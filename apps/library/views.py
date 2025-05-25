from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from apps.library.forms import ReviewsForm
from apps.library.models import Author, Book, Review


def home(request):
    return render(request, 'library/home.html')


def authors_list(request):
    authors = Author.objects.all()
    return render(request,'library/authors_list.html', {'authors': authors})


def books_list(request):
    books = Book.objects.all()
    return render(request, 'library/books_list.html', {'books': books})


def create_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            messages.success(request, 'Отзыв успешно добавлен.')
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewsForm()
    return render(request, 'library/review_form.html', {'form': form, 'book': book})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()
    return render(request, 'library/book_detail.html', {'book': book, 'reviews': reviews})


def reviews_list(request):
    reviews = Review.objects.select_related('book', 'user').all()
    return render(request, 'library/reviews_list.html', {'reviews': reviews})