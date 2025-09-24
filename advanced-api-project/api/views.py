from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters  # Import DRF filters under the 'filters' namespace
from django_filters import rest_framework as django_filters

from .models import Book
from .serializers import BookSerializer


# -------------------------------------------------------
# BookListView:
# - Handles listing all books (GET) and creating new books (POST).
# - Implements Filtering, Searching, and Ordering.
# -------------------------------------------------------
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allow read-only for unauthenticated users, write for authenticated users
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable DRF filter backends (Filtering, Searching, Ordering)
    filter_backends = [
        django_filters.DjangoFilterBackend,  # Filtering
        filters.SearchFilter,               # Searching
        filters.OrderingFilter,             # Ordering
    ]

    # Filtering: allows filtering by title, author, and publication_year
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching: allows text search by title and author
    search_fields = ['title', 'author']

    # Ordering: allows ordering results by title or publication_year
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering by title


# -------------------------------------------------------
# BookDetailView:
# - Handles retrieving a single book by ID (GET).
# -------------------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------------------------------------------
# BookCreateView:
# - Handles creating a new book (POST).
# - Restricted to authenticated users only.
# -------------------------------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -------------------------------------------------------
# BookUpdateView:
# - Handles updating an existing book (PUT/PATCH).
# - Restricted to authenticated users only.
# -------------------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -------------------------------------------------------
# BookDeleteView:
# - Handles deleting an existing book (DELETE).
# - Restricted to authenticated users only.
# -------------------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
