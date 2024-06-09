from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video_link = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField()
    course = models.ForeignKey('courses.Course', null=True, blank=True, on_delete=models.SET_NULL)
    lesson = models.ForeignKey('courses.Lesson', null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_METHOD_CHOICES = [
        ('C', 'Cash'),
        ('T', 'Transfer'),
    ]
    payment_method = models.CharField(max_length=1, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"Payment for {self.course} on {self.payment_date}"
