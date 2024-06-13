from django.shortcuts import render


from ..utils import fetch_books_with_reviews, fetch_reviews_with_books, fetch_books_and_reviews

def books_with_reviews_view(request):
    data = fetch_books_with_reviews()
    return render(request, 'Books/books_with_reviews.html', {'data': data})

def reviews_with_books_view(request):
    data = fetch_reviews_with_books()
    return render(request, 'Books/reviews_with_books.html', {'data': data})

def books_and_reviews_view(request):
    data = fetch_books_and_reviews()
    return render(request, 'Books/books_and_reviews.html', {'data': data})
