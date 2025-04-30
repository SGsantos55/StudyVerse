from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Room
from .forms import Form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signupform
from .models import Topic
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Message
from django.http import Http404

# Create your views here.
def home(request):
    topic = Topic.objects.all()
    q = request.GET.get('q', '')

    rooms = Room.objects.filter(Q(topic__topic__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    roomscount = rooms.count()
    room_messages = Message.objects.all()
    context = {
        'roomscount': roomscount,
        'rooms': rooms,
        'topic': topic,
        # 'room_messages':room_messages,
        'room_messages':Message.objects.filter(Q(room__topic__topic__icontains=q))
    }

    return render(request, 'home.html', context)

def room(request, pk):
  try:
    room = Room.objects.get(id=int(pk))
    # messages = room.message_set.all() default 
    messages = room.messages.all().order_by('-created')#most rescent messege will show first. 
    #helps to query all the child objects of room.
    participants = room.participants.all()
    
  except Room.DoesNotExist:
    return HttpResponse('Room not found.')
  if request.method=='POST':
    
      
    mess=Message.objects.create(
        user=request.user,
        room=room,
        body=request.POST.get('body')
    )
    room.participants.add(request.user)
    return redirect('room',pk=room.id)

  return render(request, 'room.html', {'room': room,'messages':messages,'participants':participants})

def Profile(request,pk):
    try:
      user = User.objects.get(id=int(pk))
      rooms = user.room_set.all() #we can access all the childrens of the class just by doing modelname_set.all or whatever.
      room_messages =user.messages.all()
      topics = Topic.objects.all() 
    except:
        return HttpResponse("User not Found")

    
    context = {
    'user':user,
    'rooms':rooms,
    'room_messages':room_messages,
    'topics':topics,

    }
    return render(request,'profile.html',context)

@login_required(login_url='login_user')
def create(request):
    page='create'
    form = Form()
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            room=form.save(commit=False)## Create a Room object but don't save it yet
            #By using commit=False, we create the object first but don’t save it, allowing us to set room.host before saving.
            room.host = request.user #Assign the currently logged-in user as the host
            room.save() #now save it to the database
            return redirect('home')
    context={
        'form':form,
        'page':page,
    }    
    return render(request, 'create.html', context)

@login_required(login_url='login_user')
def update(request, pk):
    try:
        room = Room.objects.get(id=int(pk))
    except Room.DoesNotExist:
        return HttpResponse('Room not found.')
    
    if request.user != room.host:
        messages.error(request, 'This is not your room, you are not allowed here!')
        return redirect('home')
    
    form = Form(instance=room)
    if request.method == 'POST':
        form = Form(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create.html', {'form': form})

@login_required(login_url='login_user')
def delete(request, pk):
    try:
        room = Room.objects.get(id=int(pk))
    except Room.DoesNotExist:
        return HttpResponse('Room not found.')
    
    if request.user != room.host:
        messages.error(request, 'This is not your room, you are not allowed here!')
        return redirect('home')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'delete.html', {'obj': room})

def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('santos')  # Ensure 'santos' exists in your URL patterns
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return render(request, 'login.html')
    return render(request, 'login.html', {'page': page})

def santos(request):
    if request.user.is_anonymous:
        return redirect('login_user')
    return render(request, 'home.html')

def signup_user(request):
    signup = signupform()
    if request.method == 'POST':
        sign = signupform(request.POST)
        if sign.is_valid():
            sign.save()
            return redirect('login_user')
    return render(request, 'signup.html', {'signup': signup, 'errors': signup.errors})

def logout_user(request):
    logout(request)
    return redirect('login_user')

def therock(request):
    return render(request, 'therock.html')

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

@login_required(login_url='login_user')
def delete_message(request, pk):
    message = Message.objects.filter(id=pk).first()  # Prevents crashing




    if not message:
        return HttpResponse('Message not found or already deleted.')

    if request.user != message.user:
        return HttpResponse('This is not your message, you cannot delete it!')

    if request.method == 'POST':
        room_id = message.room.id
        message.delete()
        #return redirect('room', pk=room_id)
        return redirect('home')

    return render(request, 'delete.html', {'obj': message})

