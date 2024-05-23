# user_management/urls.py
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CourseViewSet, SubscriptionAPIView
from .apps import UserManagementConfig
from django.urls import path

app_name = UserManagementConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = router.urls + [
    path('subscriptions/', SubscriptionAPIView.as_view(), name='subscription'),
]
