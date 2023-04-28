"""Tests for Models."""

from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):
    """Tests for User Model."""

    def test_create_user_with_email(self):
        """Test creating an user with email."""
        email = "test@example.com"
        password = "test123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))