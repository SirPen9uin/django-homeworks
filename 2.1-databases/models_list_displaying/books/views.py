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
    book = Book.objects.get(pub_date=pub_date)
    books = Book.objects.order_by('-pub_date')
    paginator = Paginator(books, 1)
    page_date = request.GET.get('date')
    page = paginator.get_page(page_date)
    context = {
        'book': book,
        'page': page,
    }
    return render(request, template, context)

