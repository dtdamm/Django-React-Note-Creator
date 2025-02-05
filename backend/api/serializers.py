from django.contrib.auth.models import User
from rest_framework import serializers

# Serailizer for validates user model fields
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
        extra_kwargs = {
            "password": {"write_only": True}} # Accetp password when creating user but dont return it when a user is fetched
    
    # If user is valid, create a user object
    def create(self, validated_data):
        user = User.object.create_user(**validated_data)
        return user
