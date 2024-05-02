from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import filters
from rest_framework import generics
from myproject.courses.models import Payment
from .serializers import PaymentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['payment_date']
    filterset_fields = ['course', 'lesson', 'payment_method']