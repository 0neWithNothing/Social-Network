from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    friends = models.ManyToManyField("User", blank=True)

    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=300, blank=True)
    avatar = models.ImageField(upload_to="images", null=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username



class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)


class Post(models.Model):
    image = models.ImageField(upload_to="images", null=True, blank=True)
    text = models.TextField(max_length=500, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="posts")
    date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_like')

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    likes = models.ManyToManyField(User, related_name='comment_like')

    def number_of_likes(self):
        return self.likes.count()