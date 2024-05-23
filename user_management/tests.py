from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from courses.models import Lesson, Course
from user_management.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(email='test@example.com', password='password', phone='123456789', city='City')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title='Test Course', description='Test Description', owner=self.user)
        self.lesson = Lesson.objects.create(title='Test Lesson', content='Test Content', course=self.course, owner=self.user, video_link='https://www.youtube.com/watch?v=example')

    def test_create_course(self):
        data = {'title': 'New Course', 'description': 'New Description', 'owner': self.user.id}
        response = self.client.post(reverse('course-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_lesson(self):
        data = {'title': 'New Lesson', 'content': 'New Content', 'course': self.course.id, 'owner': self.user.id, 'video_link': 'https://www.youtube.com/watch?v=new'}
        response = self.client.post(reverse('lesson-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_video_link(self):
        data = {'title': 'New Lesson', 'content': 'New Content', 'course': self.course.id, 'owner': self.user.id, 'video_link': 'https://www.invalid.com/watch?v=new'}
        response = self.client.post(reverse('lesson-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UserManagementTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            password='password123',
            phone='123456789',
            city='City'
        )
        self.course = Course.objects.create(title='Test Course')
        self.token = RefreshToken.for_user(self.user)

    def test_subscription_api(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = self.client.post('/api/subscriptions/', {'course_id': self.course.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Subscription added successfully.')

        response = self.client.post('/api/subscriptions/', {'course_id': self.course.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Subscription removed successfully.')