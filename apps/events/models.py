from django.db import models
from django.contrib.auth.models import User
from apps.categories.models import Category


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='events')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
