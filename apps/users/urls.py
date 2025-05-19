from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.users.views import register, profile, login_view

urlpatterns = [
    path('register', register, name='register'),
    path('login', login_view, name='login'),
    path('profile', profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]