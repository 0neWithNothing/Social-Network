from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string  
from django.contrib.sites.shortcuts import get_current_site  
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView
from django.core.mail import EmailMessage

from .models import User, FriendRequest
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .token import email_verification_token

# Create your views here.

class HomeView(TemplateView):
    template_name = "social/home.html"


#Creation user and sending email confirmation

class SignupUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "social/signup_user.html"

    def _send_email_verification(self, user):
        current_site = get_current_site(self.request)
        subject = 'Activate Your Account'
        body = render_to_string('email_verification.html',
            {
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': email_verification_token.make_token(user),
            }
        )
        EmailMessage(to=[user.email], subject=subject, body=body).send()

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        self._send_email_verification(user)
        return redirect("home")


#Activete user account by email

class ActivateView(View):

    def get_user_from_email_verification_token(self, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            return None

        if user is not None and email_verification_token.check_token(user, token):
            return user

        return None

    def get(self, request, uidb64, token):
        user = self.get_user_from_email_verification_token(uidb64, token)
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("home")


#Authentication users

class LoginUserView(LoginView):
    template_name = "social/login_user.html"
    authentication_form = CustomAuthenticationForm
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