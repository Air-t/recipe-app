from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """Test crating a new user with an email is successful"""

        email = "test@gmail.com"
        password = "test"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""

        email = "test@EMAilISnormaliZED.Com"
        user = get_user_model().objects.create_user(email, 'test')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test")

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@gmail.com",
            "test"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
