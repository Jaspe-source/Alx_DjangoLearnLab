from .models import Author, Book, Librarian, Library

# List all books in a library
def list_books_in_library(library):
    return Book.objects.filter(library=library)

# Query all books by a specific author
def books_by_author(author):
    return Book.objects.filter(author=author)

# Retrieve the librarian for a library
def librarian_for_library(library):
    return Librarian.objects.get(library=library)
