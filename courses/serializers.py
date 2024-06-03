from rest_framework import serializers
from .models import Course, Lesson
from .validators import validate_youtube_link

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    link = serializers.URLField(validators=[validate_youtube_link])

    class Meta:
        model = Lesson
        fields = '__all__'
