from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from user_management.paginators import CustomPageNumberPagination
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from user_management.permissions import IsOwnerOrReadOnly, IsModeratorOrReadOnly


class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsModeratorOrReadOnly]
    pagination_class = CustomPageNumberPagination

class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsOwnerOrReadOnly]

class LessonListCreate(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsModeratorOrReadOnly]
    pagination_class = CustomPageNumberPagination

class LessonRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwnerOrReadOnly]
