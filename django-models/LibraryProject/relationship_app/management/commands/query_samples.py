# relationship_app/management/commands/query_samples.py

# Import the necessary Django BaseCommand class
from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

# Define a class that inherits from BaseCommand
class Command(BaseCommand):
    # This will be the help text for your command when a user runs `python manage.py help run_queries`
    help = 'Runs sample queries and data creation for the LibraryProject models'

    # The handle() method is the main entry point for the command
    def handle(self, *args, **options):
        # The code from your original script goes here, inside this method.
        # You can use self.stdout.write() for output, which is a best practice for management commands.

        # --- Creating sample data... ---
        self.stdout.write("--- Creating sample data... ---")

        # Create a sample Author
        # Note: The model's field is 'name', not 'first_name' and 'last_name'.
        tolkien = Author.objects.get_or_create(name="J.R.R. Tolkien")[0]

        # Create a sample Library and a Librarian
        # The 'city' field does not exist in your Library model, so we remove it.
        central_library = Library.objects.get_or_create(name="Central City Library")[0]
        librarian_jane = Librarian.objects.get_or_create(name="Jane Doe", library=central_library)[0]

        # Create some Books associated with the Author and Library
        book1 = Book.objects.get_or_create(title="The Hobbit", author=tolkien, library=central_library)[0]
        book2 = Book.objects.get_or_create(title="The Lord of the Rings", author=tolkien, library=central_library)[0]

        self.stdout.write("Sample data created successfully.")
        self.stdout.write("\n")

        # --- Querying all books by J.R.R. Tolkien... ---
        self.stdout.write("--- Querying all books by J.R.R. Tolkien... ---")
        # Note: Querying on the 'name' field
        tolkien_books = Book.objects.filter(author__name="J.R.R. Tolkien")

        for book in tolkien_books:
            self.stdout.write(f"Book Title: {book.title}")
        self.stdout.write("\n")

        # --- Listing all books in Central City Library... ---
        self.stdout.write("--- Listing all books in Central City Library... ---")
        central_books = Book.objects.filter(library__name="Central City Library")

        for book in central_books:
            self.stdout.write(f"Book Title: {book.title}")
        self.stdout.write("\n")

        # --- Retrieving the librarian for Suburban Reading Corner... ---
        self.stdout.write("--- Retrieving the librarian for Central City Library... ---")
        try:
            # Use .get() to retrieve a single object
            librarian_for_library = Librarian.objects.get(library=central_library)
            self.stdout.write(f"The librarian is: {librarian_for_library.name}")
        except Librarian.DoesNotExist:
            self.stdout.write("No librarian found for this library.")

        self.stdout.write("\n--- Queries finished. ---")
