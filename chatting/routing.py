from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chatting/(?P<room_name>\S+)/$', consumers.ChatConsumer.as_asgi()),
]
