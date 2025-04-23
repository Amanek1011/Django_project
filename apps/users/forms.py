from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from apps.users.models import CustomUser

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'phone')