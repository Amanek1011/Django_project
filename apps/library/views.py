from django.http import HttpResponse
from django.shortcuts import render
from apps.library.models import Author, Book


def hello(request):
    return HttpResponse('Hello, world!')


def authors_list(request):
    authors = Author.objects.all()
    return render(request,'library/authors_list.html', {'authors': authors})

def books_list(request):
    books = Book.objects.all()
    return render(request, 'library/books_list.html', {'books': books})
