from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


@api_view(['POST'])
def register(request):
    """
    Register a new user

    POST /accounts/register
    {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "strongpassword123"
    }
    """
    data = request.data
    try:
        User.objects.create(
            username=data['username'],
            email=data['email'],
            password=make_password(data['password'])
        )
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    except:
        return Response({"error": "User creation failed"}, status=status.HTTP_400_BAD_REQUEST)