from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can access the notes
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    # If data is valid according to acceptance criteria, add the author manually since it is read only
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
            
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can access the notes
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    # If data is valid according to acceptance criteria, add the author manually since it is read only
    def perform_delete(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)    

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # Looks at all objects to make sure we dont create duplicate user
    serializer_class = UserSerializer # Serializer that tells the view how the user should be created (serlizers.py) and kind of data
    permission_classes = [AllowAny] # Allow any user to create a user, even if ther are not authenticated
