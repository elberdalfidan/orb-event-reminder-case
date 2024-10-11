from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Category objects.

    This viewset provides the standard actions for creating, retrieving, updating,
    and deleting categories. It is restricted to authenticated users, and categories
    are filtered by the logged-in user.

    Methods:
        get_queryset: Returns the queryset of categories for the authenticated user.
        perform_create: Saves a new category with the associated user.
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    queryset = Category.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
