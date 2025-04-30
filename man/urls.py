from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('',views.home,name='home'),
   path('room/<str:pk>/',views.room,name='room'),
   path('create',views.create,name='create'),
   path('update/<str:pk>/',views.update,name='update'),
   path('delete/<str:pk>/',views.delete,name='delete'),
   path('login_user',views.login_user,name='login_user'),
   path('santos',views.santos,name='santos'),
   path('signup_user',views.signup_user,name='signup_user'),
   path('logout_user',views.logout_user,name='logout_user'),
   path('therock',views.therock,name = 'therock'),
   path('delete_message/<str:pk>/',views.delete_message,name='delete_message'),
   path('profile/<str:pk>/',views.Profile,name='profile'),

   
]
