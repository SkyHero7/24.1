from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from courses.models import Lesson


class LessonAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.lesson_data = {'title': 'Test Lesson', 'description': 'Test Description'}
        self.lesson = Lesson.objects.create(title='Test Lesson', description='Test Description')

    def test_create_lesson(self):
        response = self.client.post(reverse('lesson-list'), self.lesson_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_lesson(self):
        response = self.client.get(reverse('lesson-detail', args=[self.lesson.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        updated_data = {'title': 'Updated Test Lesson'}
        response = self.client.put(reverse('lesson-detail', args=[self.lesson.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        response = self.client.delete(reverse('lesson-detail', args=[self.lesson.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
