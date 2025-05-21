from django.contrib.auth.models import AbstractUser, User
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models

from core import settings


class CustomUser(AbstractUser):
    phone = PhoneNumberField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ правильная ссылка на User
    cart = models.ManyToManyField('library.Book', related_name='in_cart', blank=True)
    favorite_books = models.ManyToManyField('library.Book', related_name='favorited_by', blank=True)
    favorite_authors = models.ManyToManyField('library.Author', related_name='favorited_by', blank=True)

    def __str__(self):
        return f"Профиль пользователя {self.user.username}"
