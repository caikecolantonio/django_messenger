from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, MessageListView

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
    path('list-messages/<str:target_identifier>/', MessageListView.as_view(), name='message-list'),
]
