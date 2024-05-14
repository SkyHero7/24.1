from rest_framework import serializers
from django.contrib.auth import get_user_model
from courses.models import Payment, Lesson
from .validators import youtube_link_validator

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[youtube_link_validator])

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'video_url', 'course']