from django.db import connection, transaction
from django.db.models import F
from django.utils import timezone
from Books.models import Review, Book, Follow, ShelfBooks, ActivityLog

def fetch_books_with_reviews():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT b.id, b.title, r.comment
            FROM "Books_book" b
            LEFT JOIN "Books_review" r ON b.id = r.book_id
        """)
        results = cursor.fetchall()
    return results

def fetch_reviews_with_books():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT r.id, r.comment, b.title
            FROM "Books_review" r
            RIGHT JOIN "Books_book" b ON r.book_id = b.id
        """)
        results = cursor.fetchall()
    return results

def fetch_books_and_reviews():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT b.id, b.title, r.comment
            FROM "Books_book" b
            FULL OUTER JOIN "Books_review" r ON b.id = r.book_id
        """)
        results = cursor.fetchall()
    return results


def fetch_books_with_avg_ratings():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT book_id, title, average_rating
            FROM books_with_avg_ratings
        """)
        results = cursor.fetchall()
    return results

def fetch_active_users():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT user_id, username, last_activity
            FROM active_users
        """)
        results = cursor.fetchall()
    return results

def fetch_books_without_reviews():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT book_id, title
            FROM books_without_reviews
        """)
        results = cursor.fetchall()
    return results

def fetch_top_5_most_followed_users():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT user_id, username, followers_count
            FROM top_5_most_followed_users
        """)
        results = cursor.fetchall()
    return results

def fetch_recent_reviews():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT review_id, comment, rating, created_at, book_title, reviewer
            FROM recent_reviews
        """)
        results = cursor.fetchall()
    return results

def add_review_and_update_count(book_id, user_id, rating, comment):
    with transaction.atomic():
        # Insert a new review
        Review.objects.create(
            book_id=book_id,
            user_id=user_id,
            rating=rating,
            comment=comment,
            created_at=timezone.now()
        )

        # Update the review count for the book
        Book.objects.filter(id=book_id).update(review_count=F('review_count') + 1)

def follow_user_and_log_activity(following_user_id, followed_user_id):
    with transaction.atomic():
        # Insert a new follow relationship
        Follow.objects.create(
            following_user_id=following_user_id,
            followed_user_id=followed_user_id,
            created_at=timezone.now()
        )

        # Log the follow activity
        ActivityLog.objects.create(
            user_id=following_user_id,
            activity=f'followed user {followed_user_id}',
            created_at=timezone.now()
        )

def transfer_book_between_shelves(book_id, from_shelf_id, to_shelf_id):
    with transaction.atomic():
        # Remove the book from the current shelf
        ShelfBooks.objects.filter(shelf_id=from_shelf_id, book_id=book_id).delete()

        # Add the book to the new shelf
        ShelfBooks.objects.create(
            shelf_id=to_shelf_id,
            book_id=book_id,
            added_at=timezone.now()
        )

