from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .apps import UserManagementConfig

app_name = UserManagementConfig.name

router = DefaultRouter()
router.register(
    r'users',
    UserViewSet,
    basename='course'
)

urlpatterns = [] + router.urls
