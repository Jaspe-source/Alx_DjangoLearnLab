from django.db import models

# The Author model represents a writer in the system.
# Each Author can be linked to multiple Book instances (One-to-Many relationship).
class Author(models.Model):
    name = models.CharField(max_length=100)  # Stores the full name of the author

    def __str__(self):
        # Display the author's name when referenced
        return self.name


# The Book model represents a published book.
# Each Book belongs to one Author (ForeignKey creates the relationship).
class Book(models.Model):
    title = models.CharField(max_length=200)  # The title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(
        Author,
        related_name="books",   # Enables reverse access: author.books.all()
        on_delete=models.CASCADE  # If an Author is deleted, delete their books too
    )

    def __str__(self):
        # Display book title and year for clarity in admin/shell
        return f"{self.title} ({self.publication_year})"
