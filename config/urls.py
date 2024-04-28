from django.urls import path, include
from rest_framework import routers
from myproject.user_management.views import UserViewSet
from myproject.courses.views import CourseViewSet, LessonListCreate, LessonRetrieveUpdateDestroy

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', LessonListCreate.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroy.as_view(), name='lesson-detail'),
]
