from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class UserRegistrationViewSetTestCase(TestCase):
    def test_user_registration(self):
        client = APIClient()
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword",
        }
        response = client.post(reverse("user-registration-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserLoginViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
        )
        self.client = APIClient()

    def test_user_login(self):
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post(reverse("user-login"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("csrf_token", response.data)

    def test_invalid_user_login(self):
        data = {"username": "testuser", "password": "wrongpassword"}
        response = self.client.post(reverse("user-login"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserLogoutViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
        )
        self.client = APIClient()

    def test_user_logout(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("user-logout"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserListViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
        )
        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_user_list(self):
        response = self.client.get(reverse("user-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
