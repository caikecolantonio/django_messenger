from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from message.models import Message

class MessageViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user', password='test_password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.recipient = User.objects.create(username='recipient_user', password='recipient_password')

    def test_create_message(self):
        data = {
            'content': 'Hello, World!',  
            'recipient': self.recipient.username,
        }
        response = self.client.post('/messages/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.first().content, 'Hello, World!')  



    def test_create_message_invalid_recipient(self):
        data = {
            'content': 'Hello, World!',
            'recipient': 'non_existent_user',
        }
        response = self.client.post('/messages/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class MessageListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='test_user', password='test_password')
        cls.recipient = User.objects.create(username='recipient_user', password='recipient_password')

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.message = Message.objects.create(
            content='Hello, World!',
            sender=self.user,
            recipient=self.recipient,
        )

    def test_message_list(self):
        response = self.client.get(f'/list-messages/{self.recipient.username}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data['results'][0]['content'], 'Hello, World!')

    def test_message_list_invalid_user(self):
        response = self.client.get('/list-messages/non_existent_user/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
