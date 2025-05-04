from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.forms import CustomUser
from apps.users.tasks import send_welcome_email
from libs.sender import send_tg_message


@receiver(post_save, sender=CustomUser)
def send_user_created(sender, instance, created, **kwargs):
    if created:
        send_welcome_email.delay(instance.email, instance.username)
        # send_tg_message("DANIK NEBE PONYATNO??? NEW USER CREATED")