from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

from apps.library.models import Book, Author
from apps.users.forms import CustomUserCreationForm
from apps.users.models import Profile


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # 👈 создаём профиль вручную
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):  # 👈 Переименовано
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # ✅ теперь это встроенная функция Django
                return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Если профиль не найден, создаем новый
        profile = Profile.objects.create(user=request.user)

    return render(request, 'users/profile.html', {
        'user': request.user,
        'cart_books': profile.cart.all(),
        'favorite_books': profile.favorite_books.all(),
        'favorite_authors': profile.favorite_authors.all(),
    })

@login_required
def add_to_cart(request, book_id):
    profile = Profile.objects.get(user=request.user)
    book = get_object_or_404(Book, id=book_id)
    profile.cart.add(book)
    messages.success(request, f'Книга «{book.name}» добавлена в корзину!')
    return redirect('books_list')


@login_required
def add_to_favorites(request, book_id=None):
    profile = Profile.objects.get(user=request.user)
    if book_id:
        book = get_object_or_404(Book, id=book_id)
        profile.favorite_books.add(book)
        messages.success(request, f'Книга «{book.name}» добавлена в избранное!')
    return redirect('books_list')

@login_required
def remove_from_cart(request, book_id):
    if request.method == 'POST':
        profile = request.user.profile
        book = get_object_or_404(Book, id=book_id)
        profile.cart.remove(book)
    return redirect('profile')

@login_required
def remove_from_favorites(request, book_id):
    if request.method == 'POST':
        profile = request.user.profile
        book = get_object_or_404(Book, id=book_id)
        profile.favorite_books.remove(book)
    return redirect('profile')