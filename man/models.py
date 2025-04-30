from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    topic=models.CharField( max_length=50)

    def __str__(self):
        return self.topic
    
class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.CASCADE)  
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)  
    name=models.CharField( max_length=50)
    participants = models.ManyToManyField(User,related_name='participants',blank=True)    

    description=models.TextField(blank=True,null=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField( auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']


    def __str__(self):
        return self.name


class Message(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE , related_name='messages')
    room = models.ForeignKey(Room, on_delete=models.CASCADE , related_name='messages')
    body = models.TextField()
    updated = models.DateTimeField( auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
      ordering = ['-updated','-created']




    def __str__(self):
        return self.body[0:60]
