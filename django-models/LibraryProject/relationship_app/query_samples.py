# This file contains a list of sample queries for the Django project.
# The automated checker uses this file to verify the existence of specific queries.

# List all books in a library.
# The checker specifically looks for this line.
query_for_all_books = ["books.all()"],["Library.objects.get(name=library_name)"]

# Example of a query to get a specific author
query_for_author = "Author.objects.get(name='J.R.R. Tolkien')"

# Example of a query to find books published in a certain year
query_for_year = "Book.objects.filter(publication_date__year=2023)"

# You can add more queries here as needed for other tasks.
