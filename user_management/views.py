from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Subscription
from .serializers import UserSerializer
from user_management.permissions import IsOwnerOrReadOnly, IsModeratorOrReadOnly
from courses.models import Course

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'list']:
            self.permission_classes = [IsAuthenticated, IsModeratorOrReadOnly]
        else:
            self.permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return super().get_permissions()

class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

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
