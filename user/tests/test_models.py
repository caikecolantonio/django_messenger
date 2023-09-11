from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword"
        )

    def test_user_creation(self):
        """Test if a user is created correctly."""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")

    def test_authentication(self):
        """Test user authentication."""
        user = User.objects.get(username="testuser")
        self.assertTrue(user.check_password("testpassword"))
        self.assertFalse(user.check_password("wrongpassword"))

    def test_str_method(self):
        """Test the __str__ method of the User model."""
        self.assertEqual(str(self.user), "testuser")
