from django.test import TestCase
from django.contrib.auth.models import User
from message.models import Message
from django.db.utils import IntegrityError

class MessageModelTestCase(TestCase):
    def setUp(self):
        self.sender_user = User.objects.create_user(username="sender", password="password1")
        self.recipient_user = User.objects.create_user(username="recipient", password="password2")

    def test_message_creation(self):
        """Test if a message is created correctly."""
        message = Message.objects.create(
            sender=self.sender_user,  
            recipient=self.recipient_user,
            content="Hello, this is a test message."
        )
        self.assertEqual(message.sender, self.sender_user)
        self.assertEqual(message.recipient, self.recipient_user)
        self.assertEqual(message.content, "Hello, this is a test message.")
        
    def test_message_timestamp(self):
        """Test if the timestamp is set correctly."""
        message = Message.objects.create(
            sender=self.sender_user,
            recipient=self.recipient_user,
            content="Another test message."
        )
        self.assertIsNotNone(message.timestamp)

    def test_message_relations(self):
        """Test related names and reverse relations."""
        message = Message.objects.create(
            sender=self.sender_user,
            recipient=self.recipient_user,
            content="Testing related names."
        )
        self.assertIn(message, self.sender_user.sent_messages.all())
        self.assertIn(message, self.recipient_user.received_messages.all())

    def test_missing_sender(self):
        """Test creating a message without a sender."""
        with self.assertRaises(IntegrityError):
            Message.objects.create(
                recipient=self.recipient_user,
                content="Missing sender test."
            )

    def test_missing_recipient(self):
        """Test creating a message without a recipient."""
        with self.assertRaises(IntegrityError):
            Message.objects.create(
                sender=self.sender_user,
                content="Missing recipient test."
            )

    def test_blank_content(self):
        """Test creating a message with blank content."""
        message = Message.objects.create(
            sender=self.sender_user,
            recipient=self.recipient_user,
            content="",
        )
        self.assertEqual(message.content, "")

    def test_str_method(self):
        """Test the __str__ method of the Message model."""
        message = Message.objects.create(
            sender=self.sender_user,
            recipient=self.recipient_user,
            content="String representation test."
        )
        expected_str = f"From {self.sender_user.username} to {self.recipient_user.username}"
        self.assertEqual(str(message), expected_str)
