from .models import Author, Book, Library, Librarian

# List all books in a library by library name
def get_books_in_library(library_name):
    # exact substring checker expects:
    library = Library.objects.get(name=library_name)
    return library.books.all()


# Query all books by a specific author by author name
def get_books_by_author(author_name):
    # exact substring checker expects:
    author = Author.objects.get(name=author_name)
    return author.books.all()


# Retrieve the librarian for a library by library name
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    # return the related one-to-one librarian
    return library.librarian
