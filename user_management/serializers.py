from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'phone', 'city', 'avatar']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

