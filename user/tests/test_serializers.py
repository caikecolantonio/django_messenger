from django.test import TestCase
from django.contrib.auth.models import User
from user.serializers import UserSerializer, UserLoginSerializer, UserRegistrationSerializer

class UserSerializerTestCase(TestCase):
    def test_user_serializer(self):
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
        }
        user = User.objects.create_user(**user_data)
        serializer = UserSerializer(instance=user)
        expected_data = {
            "username": "testuser",
            "email": "test@example.com",
        }
        self.assertEqual(serializer.data, expected_data)

class UserLoginSerializerTestCase(TestCase):
    def test_user_login_serializer(self):
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        serializer = UserLoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_user_login_serializer(self):
        data = {
            "username": "testuser",
        }
        serializer = UserLoginSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

class UserRegistrationSerializerTestCase(TestCase):
    def test_user_registration_serializer(self):
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword",
        }
        serializer = UserRegistrationSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
