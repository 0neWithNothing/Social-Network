from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
import json

from .models import Room, Message

User = get_user_model()


@login_required
def index(request):
    users = User.objects.exclude(username=request.user.username)

    return render(request, "chat/index.html", {"users": users})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[:25:-1]

    return render(request, "chat/room.html", {
        "room": room,
        "room_name_json": mark_safe(json.dumps(room.slug)),
        "username": mark_safe(json.dumps(request.user.username)),
        "messages": messages,
    })