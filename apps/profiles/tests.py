from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Profile


UserModel = get_user_model()


class ProfileTestCase(TestCase):
    def setUp(self):
        UserModel.objects.create(username="test1", email="test@test.test",
                                 password="testtest123")
        UserModel.objects.create(username="test2", email="test2@test.test",
                                 password="testtest123")

    def test_profile_created_signal(self):
        """Profile objects are created after UserModel.save()"""
        user1 = UserModel.objects.get(username="test1")
        user2 = UserModel.objects.get(username="test2")
        self.assertIsNotNone(user1.profile)
        self.assertIsNotNone(user2.profile)


class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_redirect(self):
        response = self.client.get('/')

        # check that response is redirect
        self.assertRedirects(response, '/accounts/login/?next=/')
