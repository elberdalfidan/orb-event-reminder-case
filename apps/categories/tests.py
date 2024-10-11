from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Category


class CategoryViewSetTests(APITestCase):
    """
    Test cases for the CategoryViewSet
    """
    def setUp(self):
        """
        Create a test user and authenticate the client
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)  # Fake authentication
        self.category_url = reverse('categories-list')

    def test_create_category(self):
        """
        Test creating a new category
        """
        data = {
            'name': 'Test Category',
            'description': 'A category for testing',
        }
        response = self.client.post(self.category_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Test Category')

    def test_get_categories(self):
        """
        Test getting a list of categories
        """
        Category.objects.create(name='Test Category', user=self.user)
        response = self.client.get(self.category_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_category(self):
        """
        Test updating a category
        """
        category = Category.objects.create(name='Old Category', user=self.user)
        url = reverse('categories-detail', args=[category.id])
        data = {
            'name': 'Updated Category',
            'description': 'Updated description',
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category.refresh_from_db()
        self.assertEqual(category.name, 'Updated Category')

    def test_delete_category(self):
        """
        Test deleting a category
        """
        category = Category.objects.create(name='Category to Delete', user=self.user)
        url = reverse('categories-detail', args=[category.id])  # Detaylı URL
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_get_categories_for_authenticated_user(self):
        """
        Test getting categories for the authenticated user
        """
        Category.objects.create(name='User Category', user=self.user)
        user2 = User.objects.create_user(username='testuser2', password='testpass2')
        Category.objects.create(name='Another User Category', user=user2)

        response = self.client.get(self.category_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) # only one category for the authenticated user
