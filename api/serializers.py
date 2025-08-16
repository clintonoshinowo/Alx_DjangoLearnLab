from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

# BookSerializer: Serializes all fields of the Book model.
# This serializer also includes a custom validation method to ensure
# the publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.
    Includes custom validation for the 'publication_year' field.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation method for the 'publication_year' field.
    # The 'validate_' prefix is a convention used by DRF for field-level validation.
    def validate_publication_year(self, value):
        """
        Check that the publication year is not in the future.
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer: Serializes the Author model.
# It uses a nested BookSerializer to include all related books.
# This demonstrates how to handle complex nested relationships in DRF.
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model, including a nested representation
    of all related Book objects. The 'books' field matches the
    'related_name' in the Book model's ForeignKey.
    'many=True' is used because an Author can have many Books.
    'read_only=True' means this field will be included in the serialized
    representation but will not be used to create or update the Author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
