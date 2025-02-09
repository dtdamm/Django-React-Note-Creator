from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

# Serailizer for validates user model fields
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": {"write_only": True}} # Accetp password when creating user but dont return it when a user is fetched
    
    # If user is valid, create a user object
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class NoteSerializer(serializers.Serializer):
    class Meta:
        model = Note
        fileds = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
