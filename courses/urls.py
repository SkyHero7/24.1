from django.urls import path
from rest_framework.routers import DefaultRouter


from .apps import CoursesConfig
from .views import (
    CourseViewSet,
    LessonListCreate,
    LessonRetrieveUpdateDestroy,
    PaymentList
)

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(
    r'course',
    CourseViewSet,
    basename='course'
)

urlpatterns = [
    path('lesson/', LessonListCreate.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveUpdateDestroy.as_view(), name='lesson_detail'),
    path('payments/', PaymentList.as_view(), name='payment_list'),
] + router.urls
