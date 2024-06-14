from django.shortcuts import redirect, render
from Books.models import Book, Review

from Books.utils import fetch_books_with_reviews, fetch_reviews_with_books, fetch_books_and_reviews, fetch_books_with_avg_ratings, fetch_active_users, fetch_books_without_reviews, fetch_top_5_most_followed_users, fetch_recent_reviews, add_review_and_update_count, follow_user_and_log_activity, transfer_book_between_shelves

def books_with_reviews_view(request):
    data = fetch_books_with_reviews()
    return render(request, 'Books/books_with_reviews.html', {'data': data})

def reviews_with_books_view(request):
    data = fetch_reviews_with_books()
    return render(request, 'Books/reviews_with_books.html', {'data': data})

def books_and_reviews_view(request):
    data = fetch_books_and_reviews()
    return render(request, 'Books/books_and_reviews.html', {'data': data})

def books_with_avg_ratings_view(request):
    data = fetch_books_with_avg_ratings()
    return render(request, 'Books/books_with_avg_ratings.html', {'data': data})

def active_users_view(request):
    data = fetch_active_users()
    return render(request, 'Books/active_users.html', {'data': data})

def books_without_reviews_view(request):
    data = fetch_books_without_reviews()
    return render(request, 'Books/books_without_reviews.html', {'data': data})

def top_5_most_followed_users_view(request):
    data = fetch_top_5_most_followed_users()
    return render(request, 'Books/top_5_most_followed_users.html', {'data': data})

def recent_reviews_view(request):
    data = fetch_recent_reviews()
    return render(request, 'Books/recent_reviews.html', {'data': data})


def add_review_view(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        user_id = request.POST['user_id']
        rating = request.POST['rating']
        comment = request.POST['comment']
        add_review_and_update_count(book_id, user_id, rating, comment)
        return redirect('some_view')  # Replace 'some_view' with your target view
    return render(request, 'Books/add_review.html')

def follow_user_view(request):
    if request.method == 'POST':
        following_user_id = request.POST['following_user_id']
        followed_user_id = request.POST['followed_user_id']
        follow_user_and_log_activity(following_user_id, followed_user_id)
        return redirect('some_view')  # Replace 'some_view' with your target view
    return render(request, 'Books/follow_user.html')

def transfer_book_view(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        from_shelf_id = request.POST['from_shelf_id']
        to_shelf_id = request.POST['to_shelf_id']
        transfer_book_between_shelves(book_id, from_shelf_id, to_shelf_id)
        return redirect('some_view')  # Replace 'some_view' with your target view
    return render(request, 'Books/transfer_book.html')
