from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="chats"),
    path("<slug:slug>/", views.room, name="room"),
]