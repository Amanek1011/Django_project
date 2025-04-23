from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models


class CustomUser(AbstractUser):
    phone = PhoneNumberField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.username