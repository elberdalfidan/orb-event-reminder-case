from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['GET'], url_path='upcoming')
    def upcoming_events(self, request):
        """Retrieve events happening in the next 24 hours."""
        now = timezone.now()
        upcoming_events = self.get_queryset().filter(date__gte=now, date__lt=now + timedelta(days=1))
        serializer = self.get_serializer(upcoming_events, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='category/(?P<category_name>[^/.]+)')
    def events_by_category(self, request, category_name=None):
        """Retrieve events by category."""
        events = self.get_queryset().filter(category__name=category_name)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
