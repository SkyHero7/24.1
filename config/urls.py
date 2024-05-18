from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user_management.views import MyView, SubscriptionAPIView, UserViewSet, CourseViewSet, LessonViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'lessons', LessonViewSet, basename='lesson')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_management.urls', namespace='users')),
    path('', include('courses.urls', namespace='courses')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('api/', include('user_management.urls')),
    path('my-endpoint/', MyView.as_view(), name='my-endpoint'),
    path('subscribe/', SubscriptionAPIView.as_view(), name='subscribe'),

]
