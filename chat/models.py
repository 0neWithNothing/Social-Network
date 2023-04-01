from django.db import models
from social.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
    
    class Meta:
        ordering = ('-timestamp',)