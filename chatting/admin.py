from django.contrib import admin
from .models import Message,Chat
# Register your models here.


class MessageInline(admin.StackedInline):
    model = Message


class ChatAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['token','user1','user2']}),
    ]
    inlines = [MessageInline]

admin.site.register(Chat,ChatAdmin)
