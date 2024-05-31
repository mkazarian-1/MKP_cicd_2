from django.shortcuts import render, get_object_or_404
from .models import Book
from .models import Author


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'author_detail.html', {'author': author})


def ordered_books(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'book_list_ordered.html', {'books': books})
