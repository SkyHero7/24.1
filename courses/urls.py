from django.urls import path
from .views import CourseViewSet, LessonListCreate, LessonRetrieveUpdateDestroy

urlpatterns = [
    path('courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course-list-create'),
    path('courses/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='course-detail'),
    path('lessons/', LessonListCreate.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroy.as_view(), name='lesson-detail'),
]