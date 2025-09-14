# CRUD Operations on Book Model

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>


from bookshelf.models import Book
Book.objects.all()
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>


book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>


book.delete()
# Output: (1, {'bookshelf.Book': 1})

Book.objects.all()
# Output: <QuerySet []>



