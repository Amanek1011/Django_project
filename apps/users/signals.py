from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.forms import CustomUser
from core import settings
from libs.sender import send_tg_message


@receiver(post_save, sender=CustomUser)
def send_user_created(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Hello",
            message=f"Hello {instance.username}!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )
        send_tg_message("DANIK NEBE PONYATNO??? NEW USER CREATED")