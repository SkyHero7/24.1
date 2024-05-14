from rest_framework.viewsets import ModelViewSet

from courses.serializers import CourseSerializer
from .paginators import CustomPageNumberPagination
from .serializers import UserSerializer
from rest_framework import filters
from courses.models import Payment, Course
from .serializers import PaymentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
from .models import CustomUser
from rest_framework import viewsets, permissions
from user_management.permissions import IsModerator
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsModerator | permissions.IsAdminUser]
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['payment_date']
    filterset_fields = ['course', 'lesson', 'payment_method']


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


class IsModeratorOrReadOnly:
    pass


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly | IsModeratorOrReadOnly]


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

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPageNumberPagination