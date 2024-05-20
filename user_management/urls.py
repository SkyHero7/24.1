from rest_framework.routers import DefaultRouter

from .views import UserListCreate, UserRetrieveUpdateDestroy
from .views import UserViewSet
from .apps import UserManagementConfig
from django.urls import path

app_name = UserManagementConfig.name


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls
