# Retrieve Book Instance

```python
from bookshelf.models import Book

# Retrieve all books
Book.objects.all()
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Retrieve a single book
book = Book.objects.get(title="1984")
book
# Output: <Book: 1984 by George Orwell (1949)>
