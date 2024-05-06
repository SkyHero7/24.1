from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework import filters
from myproject.courses.models import Payment
from .serializers import PaymentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from rest_framework import viewsets, permissions
from myproject.permissions import IsModerator

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsModerator | permissions.IsAdminUser]

class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['payment_date']
    filterset_fields = ['course', 'lesson', 'payment_method']



