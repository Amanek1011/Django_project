from django.urls import path

from . import views
from .views import hello

urlpatterns = [
    path('', hello, name='hello'),
    path('authors_list', views.authors_list, name='authors_list'),
    path('books_list', views.books_list, name = 'books_list')
]


