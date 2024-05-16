from rest_framework.routers import DefaultRouter

from .views import UserListCreate, UserRetrieveUpdateDestroy
from .views import UserViewSet
from .apps import UserManagementConfig
from django.urls import path

app_name = UserManagementConfig.name

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),
]

router = DefaultRouter()
router.register(
    r'users',
    UserViewSet,
    basename='user'
)

urlpatterns += router.urls
