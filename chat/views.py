from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django.db.models import Q
import json

from .models import PrivateMessage, ChatNotification

User = get_user_model()


@login_required
def index(request):
    users = request.user.friends.all()
    unread = ChatNotification.objects.filter(Q(user=request.user)&Q(is_seen=False)).count()

    return render(request, "chat/index.html", {"users": users, "unread": unread})


@login_required
def room(request, username):
    user_obj = User.objects.get(username=username)
    users = request.user.friends.all()
    unread = ChatNotification.objects.filter(Q(user=request.user)&Q(is_seen=False)).count()

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    messages = PrivateMessage.objects.filter(thread_name=thread_name)[:25:-1]

    return render(request, "chat/room.html", {"users": users, "user": user_obj, "messages": messages, "unread": unread})
    
    # room = Room.objects.get(slug=slug)
    # messages = Message.objects.filter(room=room)[:25:-1]

    # return render(request, "chat/room.html", {
    #     "room": room,
    #     "room_name_json": mark_safe(json.dumps(room.slug)),
    #     "username": mark_safe(json.dumps(request.user.username)),
    #     "messages": messages,
    # })