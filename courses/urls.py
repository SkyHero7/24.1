from django.urls import path
from .views import CourseListCreate, CourseRetrieveUpdateDestroy, LessonListCreate, LessonRetrieveUpdateDestroy

app_name = 'courses'

urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroy.as_view(), name='course-retrieve-update-destroy'),
    path('lessons/', LessonListCreate.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroy.as_view(), name='lesson-retrieve-update-destroy'),
]
