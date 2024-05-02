from rest_framework import serializers
from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.CharField(source='video_url')

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'preview', 'video_url', 'course']



class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lessons']


class PaymentSerializer:
    pass