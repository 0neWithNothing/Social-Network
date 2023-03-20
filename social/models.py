import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
# Create your models here.



class User(AbstractUser):
    friends = models.ManyToManyField("User", blank=True)

    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=300, blank=True)
    avatar = models.ImageField(upload_to="images", null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username



class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)


class Post(models.Model):
    image = models.ImageField(upload_to="images", null=True, blank=True)
    text = models.TextField(max_length=300, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="posts")
    date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_like')

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments")
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    likes = models.ManyToManyField(User, related_name='comment_like')
    date = models.DateField(auto_now=True)

    def number_of_likes(self):
        return self.likes.count()


@receiver(models.signals.post_delete, sender=Post)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Post` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=User)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `User` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = User.objects.get(pk=instance.pk).avatar
    except User.DoesNotExist:
        return False

    new_file = instance.avatar
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)