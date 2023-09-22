from django.db import models
from social.models import User

# Create your models here.


class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.thread_name
    
    class Meta:
        ordering = ('-timestamp',)


class ChatNotification(models.Model):
    chat = models.ForeignKey(PrivateMessage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username