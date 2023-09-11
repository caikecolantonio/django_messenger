from rest_framework import viewsets, status
from message.serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets
from message.models import Message
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError 
from django.http import Http404

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        recipient_identifier = self.request.data.get("recipient")
        try:
            recipient = User.objects.get(Q(username=recipient_identifier) | Q(email=recipient_identifier))
        except User.DoesNotExist:
            raise ValidationError({"error": "Recipient not found"}, code=status.HTTP_400_BAD_REQUEST)
        
        serializer.save(sender=self.request.user, recipient=recipient)



class MessageListView(ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()

    def get_queryset(self):
        target_identifier = self.kwargs.get('target_identifier')
        
        try:
            user = User.objects.get(username=target_identifier)
        except User.DoesNotExist:
            raise Http404("User does not exist")  

        queryset = Message.objects.filter(
            Q(sender=self.request.user, recipient=user) |
            Q(sender=user, recipient=self.request.user)
        ).order_by('timestamp')

        return queryset

