from django.test import TestCase
from apps.account.models import User
# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@test.com",
            password="testpassword",
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@test.com")
        self.assertTrue(self.user.check_password("testpassword"))
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.user.is_authenticated)
        self.assertTrue(self.user.is_validated)
