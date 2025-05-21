from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.users import views
from apps.users.views import register, profile_view, login_view

urlpatterns = [
    path('register', register, name='register'),
    path('login', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_favorites/book/<int:book_id>/', views.add_to_favorites, name='add_book_fav'),
    path('add_to_favorites/author/<int:author_id>/', views.add_to_favorites, name='add_author_fav'),
]