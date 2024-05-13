from .serializers import UserSerializer
from rest_framework import filters
from courses.models import Payment
from .serializers import PaymentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from rest_framework import viewsets, permissions
from permissions import IsModerator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


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