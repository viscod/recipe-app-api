from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self): # noqa
        self.client = Client()  # noqa
        self.admin_user = get_user_model().objects.create_superuser(  # noqa
            email='admin@example.com',
            password='test1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user( # noqa
            email='user@example.com',
            password='test1234'
        )

    def test_users_list(self):
        url = reverse('admin:user_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        url = reverse('admin:user_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        url = reverse('admin:user_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
