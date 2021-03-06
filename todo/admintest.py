from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            password='123',
            email='fda@gmail.com'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            username='mantis',
            password='123',
            email='111'
        )

    def test_users_listed(self):
        """Test that users are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)