from rest_framework import serializers

from user_management.models import Subscription
from .models import Course, Lesson
from .validators import validate_youtube_link

class CourseSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'is_subscribed']

    def get_is_subscribed(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False

class LessonSerializer(serializers.ModelSerializer):
    link = serializers.URLField(validators=[validate_youtube_link])

    class Meta:
        model = Lesson
        fields = '__all__'
