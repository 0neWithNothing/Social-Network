from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from .models import Room, Message

@login_required
def index(request):
    rooms = Room.objects.all()

    return render(request, "chat/index.html", {"rooms": rooms})


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