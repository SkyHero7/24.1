from django.urls import re_path, include
from rest_framework import routers

from myproject.courses.views import CourseViewSet, LessonListCreate, LessonRetrieveUpdateDestroy
from myproject.user_management.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    re_path('api/', include('courses.urls')),
    re_path('api/', include('user_management.urls')),
    re_path('', include(router.urls)),
    re_path('lessons/', LessonListCreate.as_view(), name='lesson-list-create'),
    re_path('lessons/<int:pk>/', LessonRetrieveUpdateDestroy.as_view(), name='lesson-detail'),
]
