from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    all_books = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': all_books}
    return render(request, template, context)


def one_book(request, pub_date):
    template = 'books/one_book.html'

    book = Book.objects.filter(pub_date=pub_date)

    prev_book = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    next_book = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()

    context = {
        'books': book,
        'prev_book': prev_book,
        'next_book': next_book,
    }
    return render(request, template, context)


