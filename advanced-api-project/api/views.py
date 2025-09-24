from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# BookListView
# ------------------------
# Purpose: Retrieve a list of all books in the database.
# Access: Read-only access allowed for unauthenticated users.
#         Authenticated users can also read.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# BookDetailView
# ------------------------
# Purpose: Retrieve a single book by its ID (primary key).
# Access: Read-only access allowed for unauthenticated users.
#         Authenticated users can also read.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# BookCreateView
# ------------------------
# Purpose: Create a new book entry in the database.
# Access: Restricted to authenticated users only.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# BookUpdateView
# ------------------------
# Purpose: Update an existing book’s details (by ID).
# Access: Restricted to authenticated users only.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# BookDeleteView
# ------------------------
# Purpose: Delete an existing book (by ID).
# Access: Restricted to authenticated users only.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
