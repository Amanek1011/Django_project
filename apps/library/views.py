from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.library.forms import ReviewsForm
from apps.library.models import Author, Book, Reviews


def hello(request):
    return HttpResponse('Hello, world!')


def authors_list(request):
    authors = Author.objects.all()
    return render(request,'library/authors_list.html', {'authors': authors})

def books_list(request):
    books = Book.objects.all()
    return render(request, 'library/books_list.html', {'books': books})


def create_review(request):
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews_list')
    else:
        form = ReviewsForm()

    return render(request, 'library/review_form.html', {'form': form})

def reviews_list(request):
    reviews = Reviews.objects.all().order_by('-id')
    return render(request, 'library/reviews_list.html', {'reviews': reviews})