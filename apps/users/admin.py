from django.contrib import admin

from apps.users.models import CustomUser, Profile

admin.site.register(CustomUser)
admin.site.register(Profile)
