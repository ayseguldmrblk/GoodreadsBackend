from django.db import connection

def fetch_books_with_reviews():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT b.id, b.title, r.comment
            FROM Books_book b
            LEFT JOIN Books_review r ON b.id = r.book_id
        """)
        results = cursor.fetchall()
    return results

def fetch_reviews_with_books():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT r.id, r.comment, b.title
            FROM Books_review r
            RIGHT JOIN Books_book b ON r.book_id = b.id
        """)
        results = cursor.fetchall()
    return results

def fetch_books_and_reviews():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT b.id, b.title, r.comment
            FROM Books_book b
            FULL OUTER JOIN Books_review r ON b.id = r.book_id
        """)
        results = cursor.fetchall()
    return results
