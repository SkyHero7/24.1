from django.urls import path, include
from rest_framework.routers import DefaultRouter

from courses.views import CourseListCreate, CourseRetrieveUpdateDestroy, LessonListCreate, LessonRetrieveUpdateDestroy
from .views import UserViewSet, SubscriptionAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'user_management'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('subscriptions/', SubscriptionAPIView.as_view(), name='subscription-api'),
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroy.as_view(), name='course-retrieve-update-destroy'),
    path('lessons/', LessonListCreate.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroy.as_view(), name='lesson-retrieve-update-destroy'),
]

urlpatterns += router.urls