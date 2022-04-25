from django.contrib import auth
from django.contrib.auth import login
from django.test import TestCase, Client
from django.urls import reverse

from users.models import User

# Create your tests here.
class UserRegisterTestCase(TestCase):
    client = Client()

    def setUp(self):
        # create user profile
        user1 = User.objects.create_user(username='user1', email='test@test.com', password='123')
        user1.save()

    # def test_create_user(self):
    #     user_repeat = User.objects.create_user(username='user1', email='test@test.com', password='123')
    #     user_without_password = User.objects.create_user(username='user_without_password', email='test2@test.com')
    #     user_without_email = User.objects.create_user(username='user_without_email', password='123')
    #     user_without_username = User.objects.create_user(email='test@test.com', password='123')

    def test_loading_trade(self):
        from .urls import urlpatterns

        for url in urlpatterns:
            if url.name != "logout":
                response = self.client.get(reverse(url.name))
                self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        response = self.client.post(reverse("login"), {'username': 'user1', 'password': '123', })
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

