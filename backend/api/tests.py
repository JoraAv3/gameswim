from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {
            "username": "testuser2",
            "password": "strongpassword123",
            "password2": "strongpassword123",
            "email": "test2@example.com",
            "first_name": "Test",
            "last_name": "User"
        }
        response = self.client.post("/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Пользователь успешно зарегистрирован!")
        self.assertTrue(User.objects.filter(username="testuser").exists())


class LoginTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="strongpassword123",
            email="test@example.com"
        )

    def test_login(self):
        data = {
            "username": "testuser",
            "password": "strongpassword123"
        }
        response = self.client.post("/api/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)