import random
from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Publisher

class Command(BaseCommand):
    help = 'Creates sample data for the application.'

    def handle(self, *args, **options):
        # Clear existing data to avoid duplicates
        Book.objects.all().delete()
        Author.objects.all().delete()
        Publisher.objects.all().delete()

        self.stdout.write('Deleted all existing data.')

        # Create some publishers
        publisher1 = Publisher.objects.create(name='Random House')
        publisher2 = Publisher.objects.create(name='Penguin Books')

        self.stdout.write('Created publishers.')

        # Create a few authors
        author1 = Author.objects.create(name='J.K. Rowling')
        author2 = Author.objects.create(name='George Orwell')
        author3 = Author.objects.create(name='J.R.R. Tolkien')

        self.stdout.write('Created authors.')

        # Create some books
        book1 = Book.objects.create(title='The Lord of the Rings', publisher=publisher1)
        book2 = Book.objects.create(title='1984', publisher=publisher2)
        book3 = Book.objects.create(title='Harry Potter and the Sorcerer\'s Stone', publisher=publisher1)

        # Assign authors to books
        book1.authors.add(author3)
        book2.authors.add(author2)
        book3.authors.add(author1)

        self.stdout.write('Created books and assigned authors.')

        # You can add more complex logic here if needed,
        # such as fetching external data or creating more complex relationships.

        self.stdout.write(self.style.SUCCESS('Successfully created sample data!'))

        # Print some of the newly created data to show it worked
        all_authors = Author.objects.all()
        self.stdout.write('\n--- Authors ---')
        for author in all_authors:
            self.stdout.write(f'Author: {author.name}')

        all_books = Book.objects.all()
        self.stdout.write('\n--- Books and their Authors ---')
        for book in all_books:
            author_names = ", ".join([author.name for author in book.authors.all()])
            self.stdout.write(f'Book: {book.title} (Author(s): {author_names})')
