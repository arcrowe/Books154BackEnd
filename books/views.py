from django.shortcuts import render

from .builddb import download_books_isbn
from .models import Book


def book(request):
    # type = 'hardcover-nonfiction'
    # type = 'hardcover-fiction'
    # type = 'picture-books'
    # type = 'trade-fiction-paperback'
    # type = 'paperback-nonfiction'
    # type = 'mass-market-paperback'
    # download_books_nyt(type)
    # download_books_isbn()
    # specials = Special.objects.all()
    # for book in books:
    #     for special in book.specials.all():
    #         print(special.type)
    # book = Book.objects.get(title='Great Expectations')
    # lisa = Special.objects.get(type="Lisa's Picks")
    # book.specials.add(lisa)
    # book.save()
    all_books = Book.objects.all()

    # return render(request, 'books/home.html', {'books': books, 'specials': specials})
    # return render(request, 'books/home.html', {'books': books})
    return render(request, 'books/home.html', {'books': all_books})
