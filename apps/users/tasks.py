from celery import shared_task
from django.core.mail import send_mail

from core import settings


@shared_task
def send_email():
    send_mail(
        subject="Hello",
        message=f"Hello!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['kkat51866@gmail.com'],
        fail_silently=False,
    )

@shared_task
def send_welcome_email(email: str, username: str):
    send_mail(
        subject="Hello",
        message=f"Hello {username}!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )