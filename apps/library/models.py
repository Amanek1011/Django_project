from django.conf import settings
from django.db import models

class Author(models.Model):
    name = models.CharField(
        max_length=50)
    surname = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    book_count =  models.PositiveIntegerField(
        default=0,
    )
    image = models.ImageField(
        upload_to='authors',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    book_image = models.ImageField(upload_to='books/image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.name

    class Meta:
       verbose_name = 'Book'
       verbose_name_plural = 'Books'


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв на {self.book.name} от {self.user.username}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'