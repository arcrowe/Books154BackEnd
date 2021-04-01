import json
import random

import os
import requests

from .models import Book, Special


def compute_price(search_type):
    number = 0
    if 'hard' in search_type or 'picture' in search_type:
        number = random.randint(16, 35) + .95
    elif 'paper' in search_type:
        number = random.randint(5, 13) + .95
    return number


def retrieve_nyt_google(isbns):
    length = len(isbns)
    for idx, isbn in enumerate(isbns):
        print(f'isbn {isbn}')
        if isbn['isbn10'] != 'None' and isbn['isbn10'] != '':
            isbn = str(isbn['isbn10'])
            try:
                google_request = requests.get(
                    "https:  www.googleapis.com/books/v1/volumes?q=isbn:" + isbn + "&key=" + os.environ.get(
                        'GOOGLE_BOOKS')
                )
                google_book = json.loads(google_request.content)
                cover = "http:  covers.openlibrary.org/b/isbn/" + str(isbn) + ".jpg"
                test = requests.get(cover)
                if google_book["totalItems"] != 0:
                    if test.status_code != 500:
                        return isbn, google_book['items'][0]['volumeInfo'], cover
                    else:
                        if length - 1 == idx:
                            cover = google_book['items'][0]['volumeInfo']['imageLinks']['thumbnail']
                            return isbn, google_book['items'][0]['volumeInfo'], cover
                        continue
            except:
                continue

    return None


def retrieve_isbn_google(isbn):
    print(isbn)
    google_request = requests.get(
        "https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn + "&key=" + os.environ.get(
            'GOOGLE_BOOKS')
    )
    google_book = json.loads(google_request.content)
    print(google_book)
    cover = "http://covers.openlibrary.org/b/isbn/" + str(isbn) + ".jpg"
    test = requests.get(cover)
    print(f'isbn {isbn} - google # items - {google_book["totalItems"]}')
    if google_book["totalItems"] != 0:
        if test.status_code == 500:
            cover = google_book['items'][0]['volumeInfo']['imageLinks']['thumbnail']
        return isbn, google_book['items'][0]['volumeInfo'], cover
    else:
        return None


def download_books_nyt(search_type: str):
    api_request = requests.get(
        "https://api.nytimes.com/svc/books/v3/lists.json?list-name=" + search_type + "&api-key=" +
        os.environ.get('NYT_BOOKS'))
    nyt = json.loads(api_request.content)
    for result in nyt['results']:
        try:
            isbn, google_items, cover = retrieve_nyt_google(result['isbns'])
            pubDate = google_items['publishedDate']
            if len(pubDate) == 4:
                pubDate = pubDate + '-01-01'
            elif len(pubDate) == 7:
                pubDate = pubDate + '-01'

            if 'hard' in search_type or 'picture' in search_type:
                book_format = 'Hard Cover'
            else:
                book_format = 'Paperback'

            book = Book(title=result['book_details'][0]['title'],
                        authors=result['book_details'][0]['author'],
                        isbn=isbn,
                        short_description=result['book_details'][0]['description'],
                        subtitle=google_items.get('subtitle', ''),
                        long_description=google_items['description'],
                        publisher=result['book_details'][0]['publisher'],
                        publishedDate=pubDate,
                        category=google_items.get('categories', ['Fiction'])[0],
                        pageCount=google_items['pageCount'],
                        format=book_format,
                        language=google_items['language'],
                        price=compute_price(search_type),
                        cover=cover)
            try:
                Book.objects.get(isbn=isbn)
            except Book.DoesNotExist:
                book.save()
        except:
            continue


def download_books_isbn():
    # these are paperbacks
    oprah = ["1451654561", "0061804819", "0809073641", "0307401944", "0060391626", "0451488334", "1405528966",
             "1440631328", "0446587427", "0307267458", "0060740450", "1101911115", "0198748841", "0307523632",
             "1400032970", "0375726977", "0393070352", "0316025674", "0307386589", "1782394877", "1400079012",
             "0062254421", "1772753904", "1101213132", "0307388123", "1451641656", "0670024783", "0486415864",
             "0743262441", "1101199563", "0547346654", "1400077702", "0307792153", "155199853X", "1448105021",
             "0307764060", "1101200189", "1440673241", "0375505873", "1588369242", "0399590609", "1250209765"]
    natbook = ["1250309883", "0735219451", "0345804325", "0143126822", "1101616180", "1501126067", "0812997484",
               "0062065262", "0062065262", "1408841312", "0307946738", "0812973992", "1588368246", "0374279128",
               "1101118199", "0061750301", "0374706352", "0375422420", "0312273207"]
    booker = ["0571348491", "0349130221", "0307370569", "0307794237", "1590173732", "0747578249",
              "1407090488", "1619028220", "1939140560", "022606817X", "1409043584", "0547525508", "0374526400",
              "0307367754", "1848940203", "0307826228", "0807130729", "0141044845", "0307787133", "0307576183",
              "0307819566", "1504040201", "1504040201"]
    favorites_paperback = ["0521732557", "030747772X", "0812985532", "0394820371", "1506710182", "0805099794",
                           "0007204493",
                           "1451673264", "0062368680", "087113361X", "1107096820", "0684818701"]

    # these are hardbacks
    favorites_hardcover = ["1501178415", "006293127X"]
    for isbntofind in natbook:
        search_type = 'paperback'  "****** don't forget to change *******"
        isbn, google_items, cover = retrieve_isbn_google(isbntofind)
        pubDate = google_items['publishedDate']
        if len(pubDate) == 4:
            pubDate = pubDate + '-01-01'
        elif len(pubDate) == 7:
            pubDate = pubDate + '-01'

        if 'hard' in search_type or 'picture' in search_type:
            book_format = 'Hard Cover'
        else:
            book_format = 'Paperback'

        book = Book(title=google_items["title"],
                    authors=google_items["authors"][0],
                    isbn=isbn,
                    short_description='',
                    subtitle=google_items.get('subtitle', ''),
                    long_description=google_items['description'],
                    publisher=google_items.get("publisher", 'UnKnown'),
                    publishedDate=pubDate,
                    category=google_items.get('categories', ['Fiction'])[0],
                    pageCount=google_items['pageCount'],
                    format=book_format,
                    language=google_items['language'],
                    price=compute_price(search_type),
                    cover=cover,
                    )
        cat = Special.objects.get(type="National Book Award")
        try:
            Book.objects.get(isbn=isbn)
        except Book.DoesNotExist:
            book.save()
            book.specials.add(cat)
            book.save()
