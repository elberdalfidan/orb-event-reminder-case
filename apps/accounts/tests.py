from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class AuthTests(APITestCase):
    def setUp(self):
        """
        Set up necessary data for the tests.
        This method is run before each test case.
        """
        self.register_url = reverse('account_register')  # 'register' should match the name in your urls.py
        self.login_url = reverse('token_obtain_pair')  # 'token_obtain_pair' is the JWT login endpoint

        # Test user data
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "strongpassword123"
        }

    def test_user_registration(self):
        """
        Test user registration with valid data.
        """
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "User created successfully")

        # Check if the user was created in the database
        self.assertTrue(User.objects.filter(username=self.user_data['username']).exists())

    def test_user_registration_with_missing_data(self):
        """
        Test user registration with missing required fields.
        """
        incomplete_data = {
            "username": "testuser2",
            "email": ""  # Email is missing
        }
        response = self.client.post(self.register_url, incomplete_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login(self):
        """
        Test user login with valid credentials.
        """
        # Register a new user
        self.client.post(self.register_url, self.user_data, format='json')

        # Test login
        login_data = {
            "username": self.user_data['username'],
            "password": self.user_data['password']
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that we get the access and refresh tokens
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_login_with_invalid_credentials(self):
        """
        Test user login with invalid credentials.
        """
        # Register a new user
        self.client.post(self.register_url, self.user_data, format='json')

        # Attempt login with incorrect password
        login_data = {
            "username": self.user_data['username'],
            "password": "wrongpassword"
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "No active account found with the given credentials")
