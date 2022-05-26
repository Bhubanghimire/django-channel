# chat/routing.py
from django.urls import re_path
from django.urls import path, include
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/<str:room_name2>/', consumers.ChatConsumer.as_asgi()),
]