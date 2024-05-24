from django.urls import path
from .views import CourseListCreate, CourseRetrieveUpdateDestroy, LessonRetrieveUpdateDestroy, PaymentList

app_name = 'courses'

urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroy.as_view(), name='course-retrieve-update-destroy'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroy.as_view(), name='lesson-retrieve-update-destroy'),
    path('payments/', PaymentList.as_view(), name='payment-list'),
]