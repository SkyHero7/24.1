from django.urls import path
from rest_framework.routers import DefaultRouter


from .apps import CoursesConfig
from .views import (
    LessonListCreate,
    LessonRetrieveUpdateDestroy,
    PaymentList
)

app_name = CoursesConfig.name



urlpatterns = [
    path('lesson/', LessonListCreate.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveUpdateDestroy.as_view(), name='lesson_detail'),
    path('payments/', PaymentList.as_view(), name='payment_list'),
]
