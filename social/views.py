# from django.shortcuts import render
# from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm

from .models import User, FriendRequest
from .forms import CustomUserCreationForm

# Create your views here.

class HomeView(TemplateView):
    template_name = "social/home.html"



#Creation and Authentication users

class SignupUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "social/signup_user.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect('')


class LoginUserView(LoginView):
    template_name = "social/login_user.html"
    authentication_form = AuthenticationForm
    next_page = "home"


class LogoutUserView(LogoutView):
    template_name = "social/login_user.html"
    next_page = "home"


#List all users

class UsersListView(ListView):
    model = User
    template_name = "social/users_list.html"
    context_object_name = "users"





#Two functions below for sending and accepting friend requests

@login_required
def send_friend_request(request, id):
    from_user = request.user
    to_user = User.objects.get(id=id)
    if to_user not in from_user.friends.all():
        friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
        if created:
            return HttpResponse("Friend request sent!")
    else:
        from_user.friends.remove(to_user)
        to_user.friends.remove(from_user)
    return HttpResponse("Friend request was already sent!")


@login_required
def accept_friend_request(request, id):
    friend_request = FriendRequest.objects.get(id=id)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse("Friend request accepted!")
    else:
        return HttpResponse("Friend request not accepted!")