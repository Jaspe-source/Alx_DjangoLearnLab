from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints.
    Covers CRUD, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")

        # Create an Author
        self.author = Author.objects.create(name="John Doe")

        # Create a Book
        self.book = Book.objects.create(
            title="Sample Book",
            publication_year=2020,
            author=self.author
        )

        # URL patterns
        self.list_url = reverse("book-list")   # /books/
        self.detail_url = reverse("book-detail", args=[self.book.id])  # /books/<id>/
        self.create_url = reverse("book-create")  # /books/create/
        self.update_url = reverse("book-update", args=[self.book.id])  # /books/update/<id>/
        self.delete_url = reverse("book-delete", args=[self.book.id])  # /books/delete/<id>/

    # ----------------------
    # CRUD TESTS
    # ----------------------

    def test_list_books(self):
        """Test retrieving the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Sample Book", str(response.data))

    def test_retrieve_book_detail(self):
        """Test retrieving a single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Sample Book")

    def test_create_book_authenticated(self):
        """Test creating a new book (authenticated)"""
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Test unauthenticated users cannot create a book"""
        self.client.logout()
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating an existing book"""
        data = {
            "title": "Updated Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ----------------------
    # FILTER, SEARCH, ORDER
    # ----------------------

    def test_filter_books_by_title(self):
        """Test filtering books by title"""
        response = self.client.get(self.list_url, {"title": "Sample Book"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Sample Book")

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get(self.list_url, {"search": "Sample"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Sample Book", str(response.data))

    def test_order_books_by_year(self):
        """Test ordering books by publication_year"""
        # Create another book with earlier year
        Book.objects.create(title="Older Book", publication_year=2010, author=self.author)
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Ensure the first book in list is the older one
        self.assertEqual(response.data[0]["title"], "Older Book")
