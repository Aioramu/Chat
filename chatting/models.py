from django.db import models
from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()



class Chat(models.Model):
    token=models.CharField(max_length=200)
    user1=models.CharField(max_length=200,default='admin')
    user2=models.CharField(max_length=200,default='admin')

class Message(models.Model):
    chat = models.ForeignKey(Chat, default=0, related_name='message',on_delete=models.CASCADE)
    content = models.TextField(default='Hello')
    timestamp = models.DateTimeField(auto_now_add=True)
