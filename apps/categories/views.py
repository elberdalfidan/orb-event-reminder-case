from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer
from rest_framework.exceptions import ValidationError


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
        # Check if a category with the same name already exists for the user
        category_name = serializer.validated_data.get('name')
        if self.get_queryset().filter(name=category_name).exists():
            raise ValidationError({'message': f"A category with the name '{category_name}' already exists."})
        serializer.save(user=self.request.user)
