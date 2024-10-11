from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Event, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class EventTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.category1 = Category.objects.create(name='Category 1', user=self.user)
        self.category2 = Category.objects.create(name='Category 2', user=self.user)

        self.event1 = Event.objects.create(
            title='Event 1',
            date='2024-10-12T12:00:00Z',
            category=self.category1,
            user=self.user
        )
        self.event2 = Event.objects.create(
            title='Event 2',
            date='2024-10-11T10:00:00Z',
            category=self.category2,
            user=self.user
        )

    def test_create_event(self):
        """POST /events - Create a new event reminder."""
        url = reverse('events-list')
        data = {
            'title': 'New Event',
            'date': '2024-10-15T10:00:00Z',
            'category': self.category1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_upcoming_events(self):
        """GET /events/upcoming - Retrieve events happening in the next 24 hours."""
        url = reverse('events-upcoming-events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.event1.title, [event['title'] for event in response.data])
        self.assertNotIn(self.event2.title, [event['title'] for event in response.data])

    def test_events_by_category(self):
        """GET /events/category/{categoryName} - Retrieve events by category."""
        url = reverse('events-events-by-category', args=[self.category1.name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.event1.title, [event['title'] for event in response.data])
        self.assertNotIn(self.event2.title, [event['title'] for event in response.data])

    def test_events_by_nonexistent_category(self):
        """GET /events/category/{categoryName} - Test with a non-existent category."""
        url = reverse('events-events-by-category', args=['NonExistentCategory'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
