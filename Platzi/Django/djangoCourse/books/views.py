from django.shortcuts import render
from .models import Book


def get_books(request):
    books = Book.objects.all()
    context = {'books_list': books}
    return render(request, 'books_template.html', context)
