from datetime import timezone, timedelta

from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from user_management.models import CustomUser


@shared_task
def send_course_update_email(course_id, user_emails):
    subject = 'Course Updated'
    message = 'The course you are subscribed to has been updated.'
    email_from = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, email_from, user_emails)

@shared_task
def check_last_login():
    one_month_ago = timezone.now() - timedelta(days=30)
    users_to_deactivate = CustomUser.objects.filter(last_login__lt=one_month_ago, is_active=True)
    users_to_deactivate.update(is_active=False)

def deactivate_inactive_users():
    User = get_user_model()
    one_month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)
    inactive_users.update(is_active=False)
    return f"Deactivated {inactive_users.count()} inactive users."