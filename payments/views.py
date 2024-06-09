from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import create_stripe_product, create_stripe_price, create_stripe_session
from .models import Payment
from courses.models import Course
from django.conf import settings

class CreatePaymentView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course_id')
        course = Course.objects.get(id=course_id)

        stripe_product_id = create_stripe_product(course.name)
        stripe_price_id = create_stripe_price(stripe_product_id, int(course.price * 100))  # Price in cents

        success_url = f"{settings.FRONTEND_URL}/payment-success/"
        cancel_url = f"{settings.FRONTEND_URL}/payment-cancel/"
        stripe_session_id, stripe_session_url = create_stripe_session(stripe_price_id, success_url, cancel_url)

        payment = Payment.objects.create(
            user=user,
            course=course,
            stripe_product_id=stripe_product_id,
            stripe_price_id=stripe_price_id,
            stripe_session_id=stripe_session_id
        )

        return Response({'stripe_session_url': stripe_session_url}, status=status.HTTP_201_CREATED)