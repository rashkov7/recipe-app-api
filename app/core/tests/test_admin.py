"""
Tests for the Django admin modifications.
More information about testing admin panel can be found here:
https://docs.djangoproject.com/en/3.2/topics/testing/tools/#overview-and-a-quick-example
https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#reversing-admin-urls
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


User = get_user_model()
class AdminSiteTests(TestCase):
    """Test the user model admin"""
    def setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user = User.objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_lists(self):
        """Test that users are listed on page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page """

        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)
        self.assertContains(res, self.user.email)

    def test_create_user_page(self):
        """Test create users page"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)
