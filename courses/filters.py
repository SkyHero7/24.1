import django_filters
from .models import Payment

class PaymentFilter(django_filters.FilterSet):
    payment_date = django_filters.DateFilter(field_name='payment_date')
    course = django_filters.NumberFilter(field_name='course')
    lesson = django_filters.NumberFilter(field_name='lesson')
    payment_method = django_filters.CharFilter(field_name='payment_method')

    class Meta:
        model = Payment
        fields = ['payment_date', 'course', 'lesson', 'payment_method']
