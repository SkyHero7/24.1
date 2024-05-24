from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SubscriptionAPIView
from .apps import UserManagementConfig
from django.urls import path

app_name = UserManagementConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


urlpatterns = router.urls + [
    path('subscriptions/', SubscriptionAPIView.as_view(), name='subscription'),
]
