from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class UserURLsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
        )

    def test_user_registration_url(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword",
        }
        response = self.client.post('/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login_url(self):
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post('/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_logout_url(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list_url(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get('/users-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
