from django.urls import include, path
from rest_framework.routers import DefaultRouter

from message.views import send_message
from message.viewsets import Chat_roomViewSet, MessageViewSet

router = DefaultRouter()

router.register(r'chat_rooms', Chat_roomViewSet,basename='chat_rooms')
router.register(r'messages', MessageViewSet,basename='message')

urlpatterns = [
    path('', include(router.urls)),
    path('send_message/', send_message, name='send_message'),
]