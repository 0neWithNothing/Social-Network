# from django.shortcuts import render
# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm

from .models import User
from .forms import CustomUserCreationForm

# Create your views here.

class HomeView(TemplateView):
    template_name = "social/home.html"


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




def send_friend_request(request, id):
    pass


def accept_friend_request(request, id):
    pass