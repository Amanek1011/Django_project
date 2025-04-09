from django.contrib import admin

# Register your models here.

from apps.library.models import *

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'book_count')
    list_display_links = ('name','surname', 'book_count')
    list_filter = ('name', 'surname', 'book_count')
    search_fields = ('name', 'surname')
    ordering = ('id', 'name', 'surname')

@admin.register(Book)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name')
    list_display_links = ('id', 'author', 'name')
    list_filter = ('id', 'author', 'name')
    search_fields = ('id', 'author', 'name')
    ordering = ('id', 'author', 'name')