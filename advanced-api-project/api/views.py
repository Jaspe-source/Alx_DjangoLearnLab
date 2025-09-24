from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters  # 👈 add this import
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    BookListView
    ------------------------
    Purpose:
        Retrieve a list of all books with advanced query capabilities:
        - Filtering
        - Searching
        - Ordering

    Features:
        1. Filtering
            Allows filtering by 'title', 'author', and 'publication_year'.
            Example: /api/books/?title=Clean Code&publication_year=2008

        2. Searching
            Enables text search on 'title' and 'author'.
            Example: /api/books/?search=Martin

        3. Ordering
            Supports sorting results by 'title' or 'publication_year'.
            Example: /api/books/?ordering=title
            Example: /api/books/?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields allowed for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields allowed for search
    search_fields = ['title', 'author']

    # Fields allowed for ordering
    ordering_fields = ['title', 'publication_year']

    # Default ordering (newest books first by year)
    ordering = ['publication_year']
