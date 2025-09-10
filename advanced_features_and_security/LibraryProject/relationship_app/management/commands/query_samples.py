import random
from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    help = 'Creates sample data and runs a few queries to demonstrate model relationships.'

    def handle(self, *args, **options):
        # Clear existing data to ensure a fresh start
        Book.objects.all().delete()
        Author.objects.all().delete()
        Library.objects.all().delete()
        Librarian.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('--- Creating sample data... ---'))

        # Create authors
        tolkien, created = Author.objects.get_or_create(name='J.R.R. Tolkien', defaults={'email': 'tolkien@example.com'})
        rowling, created = Author.objects.get_or_create(name='J.K. Rowling', defaults={'email': 'rowling@example.com'})
        martin, created = Author.objects.get_or_create(name='George R.R. Martin', defaults={'email': 'martin@example.com'})

        # Create books and assign authors
        Book.objects.get_or_create(title='The Hobbit', author=tolkien)
        Book.objects.get_or_create(title='The Lord of the Rings', author=tolkien)
        Book.objects.get_or_create(title='Harry Potter and the Philosopher\'s Stone', author=rowling)
        Book.objects.get_or_create(title='A Game of Thrones', author=martin)

        # Create libraries
        central_library, created = Library.objects.get_or_create(name='Central City Library')
        university_library, created = Library.objects.get_or_create(name='University Library')

        # Create librarians and assign them to libraries
        Librarian.objects.get_or_create(name='Jane Doe', library=central_library)
        Librarian.objects.get_or_create(name='John Smith', library=university_library)
        
        # Add books to libraries
        all_books = Book.objects.all()
        for book in all_books:
            # Randomly assign books to libraries
            if random.random() < 0.5:
                central_library.books.add(book)
            else:
                university_library.books.add(book)

        self.stdout.write(self.style.SUCCESS('Sample data created successfully.'))

        self.stdout.write(self.style.SUCCESS('\n--- Querying all books by J.R.R. Tolkien... ---'))
        tolkien_books = Book.objects.filter(author=tolkien)
        if tolkien_books.exists():
            for book in tolkien_books:
                self.stdout.write(f'Book Title: {book.title}')
        else:
            self.stdout.write('No books found for this author.')

        self.stdout.write(self.style.SUCCESS('\n--- Listing all books in Central City Library... ---'))
        try:
            central_lib = Library.objects.get(name='Central City Library')
            if central_lib.books.exists():
                for book in central_lib.books.all():
                    self.stdout.write(f'Book Title: {book.title}')
            else:
                self.stdout.write('Central City Library has no books.')
        except Library.DoesNotExist:
            self.stdout.write('Central City Library not found.')

        self.stdout.write(self.style.SUCCESS('\n--- Retrieving the librarian for Central City Library... ---'))
        try:
            central_librarian = Librarian.objects.get(library=central_library)
            self.stdout.write(f'The librarian is: {central_librarian.name}')
        except Librarian.DoesNotExist:
            self.stdout.write('No librarian found for Central City Library.')
        except Librarian.MultipleObjectsReturned:
            self.stdout.write('Multiple librarians found for Central City Library.')

        self.stdout.write(self.style.SUCCESS('\n--- Queries finished. ---'))
