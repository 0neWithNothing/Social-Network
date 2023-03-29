from django.db import models
from social.models import User

# Create your models here.

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
    
    def last_20_messages(self):
        return Message.objects.order_by('-timestamp').all()[:20]