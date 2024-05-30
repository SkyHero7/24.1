from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from courses.models import Lesson, Course
from courses.serializers import LessonSerializer
from .models import CustomUser, Subscription
from .serializers import UserSerializer
from user_management.permissions import IsOwnerOrReadOnly, IsModeratorOrReadOnly
from django.utils.crypto import get_random_string


class UserListView(APIView):
    permission_classes = [IsAuthenticated | IsModeratorOrReadOnly]

    def get(self, request):
        if request.user.groups.filter(name='Модераторы').exists():
            users = CustomUser.objects.all()
        else:
            users = CustomUser.objects.filter(id=request.user.id)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        course_id = request.data.get('course_id')
        course = get_object_or_404(Course, pk=course_id)

        subscription, created = Subscription.objects.get_or_create(user=user, course=course)

        if created:
            message = 'Subscription added successfully.'
        else:
            subscription.delete()
            message = 'Subscription removed successfully.'

        return Response({'message': message}, status=status.HTTP_200_OK)


class UserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class SendVerificationEmailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        token = get_random_string(length=32)
        user.verification_token = token
        user.is_active = False
        user.save()

        verification_url = request.build_absolute_uri(
            reverse('verify-email', kwargs={'token': token})
        )
        send_mail(
            subject='Verify your email',
            message=f'Please verify your email by clicking the following link: {verification_url}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )

        return Response({'message': 'Verification email sent.'}, status=status.HTTP_200_OK)


class VerifyEmailView(APIView):

    def get(self, request, token):
        user = get_object_or_404(CustomUser, verification_token=token)
        user.is_active = True
        user.verification_token = ''
        user.save()

        return Response({'message': 'Email verified successfully.'}, status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [IsAuthenticated]


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [IsAuthenticated]

