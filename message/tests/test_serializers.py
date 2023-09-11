from django.test import TestCase
from django.contrib.auth.models import User 
from message.models import Message
from message.serializers import MessageSerializer 

class MessageSerializerTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender_user', password='sender_password')
        self.recipient = User.objects.create_user(username='recipient_user', password='recipient_password')

    def test_message_serializer(self):
        self.client.login(username='sender_user', password='sender_password')
        message_data = {
            'content': 'Test message content',
            'sender': self.sender,
            'recipient': self.recipient,
        }
        message = Message.objects.create(**message_data)

        serializer = MessageSerializer(message)

        serialized_data = serializer.data
        self.assertEqual(serialized_data['content'], 'Test message content')
