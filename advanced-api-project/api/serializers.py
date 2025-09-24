from rest_framework import serializers
from .models import Author, Book
import datetime


# Serializer for the Book model
# Converts Book instances into JSON and validates input data.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to prevent future publication years
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# Serializer for the Author model
# Includes author's name and dynamically serializes related books
# using the nested BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    # books field shows all books related to the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
