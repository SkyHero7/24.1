from rest_framework import serializers
from .models import Course, Lesson
from courses.models import Payment
from .validators import youtube_link_validator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'preview', 'video_link', 'course']



class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lessons', 'lessons_count']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[youtube_link_validator])

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'video_url', 'course']
