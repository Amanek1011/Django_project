from django.urls import path

from . import views
from .views import create_review,home

urlpatterns = [
    path('', views.home, name='home'),
    path('authors_list', views.authors_list, name='authors_list'),
    path('books_list', views.books_list, name='books_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/review/add/', views.create_review, name='create_review'),
    path('reviews/', views.reviews_list, name='reviews_list'),
]
