from rest_framework.viewsets import ModelViewSet

from courses.serializers import CourseSerializer, LessonSerializer
from .paginators import CustomPageNumberPagination
from .serializers import UserSerializer
from courses.models import Course, Lesson
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
from .models import CustomUser
from rest_framework import viewsets, permissions
from user_management.permissions import IsModerator, IsOwnerOrReadOnly, IsModeratorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated, IsModeratorOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]




class UserListView(APIView):
    permission_classes = [IsAuthenticated | IsModerator]

    def get(self, request):
        if request.user.groups.filter(name='Модераторы').exists():
             users = CustomUser.objects.all()
        else:
            users = CustomUser.objects.filter(id=request.user.id)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class MyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'message': 'Этот эндпоинт закрыт авторизацией'})




class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'list']:
            self.permission_classes = [IsAuthenticated, IsModerator]
        else:
            self.permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return super().get_permissions()


class SubscriptionAPIView(APIView):
    def post(self, request):
        user = request.user
        course_id = request.data.get('course_id')
        course = Course.objects.get(pk=course_id)

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

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'list']:
            self.permission_classes = [IsAuthenticated, IsModerator]
        else:
            self.permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return super().get_permissions()