from django.contrib import admin

from .models import PrivateMessage, ChatNotification
# Register your models here.

admin.site.register(PrivateMessage)
admin.site.register(ChatNotification)
