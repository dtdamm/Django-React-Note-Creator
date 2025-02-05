from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # Looks at all objects to make sure we dont create duplicate user
    serializer_class = User # Serializer that tells the view how the user should be created (serlizers.py) and kind of data
    permission_classes = [AllowAny] # Allow any user to create a user, even if ther are not authenticated
