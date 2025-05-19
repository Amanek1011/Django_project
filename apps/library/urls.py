from django.urls import path

from . import views
from .views import hello, create_review

urlpatterns = [
    path('', hello, name='hello'),
    path('authors_list', views.authors_list, name='authors_list'),
    path('books_list', views.books_list, name = 'books_list'),
    path('review/add/', views.create_review, name='create_review'),
    path('reviews/', views.reviews_list, name='reviews_list'),
]


