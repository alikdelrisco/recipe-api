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

    def test_create_user_email_required(self):
        """Test user email required."""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password='test123',
            )

    def test_create_superuser(self):
        """Test superuser creation."""
        user = get_user_model().objects.create_superuser(
            'admin@example.com',
            'admin123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
