from django.urls import path
from user_management.views import (
    UserListView,
    SubscriptionAPIView,
    UserListCreate,
    UserRetrieveUpdateDestroy,
    SendVerificationEmailView,
    VerifyEmailView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('subscribe/', SubscriptionAPIView.as_view(), name='subscribe'),
    path('users/create/', UserListCreate.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('send-verification-email/', SendVerificationEmailView.as_view(), name='send-verification-email'),
    path('verify-email/<str:token>/', VerifyEmailView.as_view(), name='verify-email'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]