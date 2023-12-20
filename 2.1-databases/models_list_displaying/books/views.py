from django.shortcuts import render
from books.models import Book


def books_view(request):
    all_books = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': all_books}
    return render(request, template, context)


def one_book(request, pub_date):
    template = 'books/one_book.html'
    books = Book.objects.get(pub_date=pub_date)
    context = {
        'book': books
    }
    return render(request, template, context)

