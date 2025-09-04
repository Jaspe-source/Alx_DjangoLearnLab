from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # show these columns in admin
    search_fields = ('title', 'author')                      # allow search by title and author
    list_filter = ('publication_year',)                      # filter by year
