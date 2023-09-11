from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from message.models import Message

class MessageURLsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')  


    def test_message_viewset_urls(self):
        message = Message.objects.create(
            sender=self.user,
            recipient=self.user,
            content="Test message",
        )

        detail_url = reverse('message-detail', kwargs={'pk': message.pk})
        self.assertEqual(detail_url, f'/messages/{message.pk}/')
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
