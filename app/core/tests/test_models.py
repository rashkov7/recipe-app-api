from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()
class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""

        email = 'test@example.com'
        password = 'password1234'
        user = User.objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""


        sample_emails = (
            ('test1@EXAMPLE.com', 'test1@example.com'),
            ('Test2@Example.com', 'Test2@example.com'),
            ('TEST3@EXAMPLE.com', 'TEST3@example.com'),
            ('test4@example.COM', 'test4@example.com'),
        )

        for email, expected in sample_emails:
            user = User.objects.create_user(email=email, password='password1234')

            self.assertEqual(user.email, expected)

    def test_new_user_invalid_email(self):

        """Test creating user with no email raises exception"""
        with self.assertRaises(ValueError) as ex:
            User.objects.create_user(email=None, password='password1234')
        self.assertEqual(str(ex.exception), "Email field could not be empty.")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = User.objects.create_superuser(email='test@example.com', password='password1234')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)