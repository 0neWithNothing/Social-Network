from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    friends = models.ManyToManyField("User", blank=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)


