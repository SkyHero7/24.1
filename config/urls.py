from django.contrib import admin
from django.urls import path, include
from user_management.models import UserListCreate, UserRetrieveUpdateDestroy
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_management.urls', namespace='users')),
    path('', include('courses.urls', namespace='courses')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('user_management.urls')),

]
