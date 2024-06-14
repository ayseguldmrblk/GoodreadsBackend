"""
URL configuration for Goodreads project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Import views from the Books app
from Books.views import books_with_reviews_view, reviews_with_books_view, books_and_reviews_view, books_with_avg_ratings_view, active_users_view, books_without_reviews_view, top_5_most_followed_users_view, recent_reviews_view, add_review_view, follow_user_view, transfer_book_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books_with_reviews/', books_with_reviews_view, name='books_with_reviews'),
    path('reviews_with_books/', reviews_with_books_view, name='reviews_with_books'),
    path('books_and_reviews/', books_and_reviews_view, name='books_and_reviews'),
    path('books_with_avg_ratings/', books_with_avg_ratings_view, name='books_with_avg_ratings'),
    path('active_users/', active_users_view, name='active_users'),
    path('books_without_reviews/', books_without_reviews_view, name='books_without_reviews'),
    path('top_5_most_followed_users/', top_5_most_followed_users_view, name='top_5_most_followed_users'),
    path('recent_reviews/', recent_reviews_view, name='recent_reviews'),
    path('add_review/', add_review_view, name='add_review'),
    path('follow_user/', follow_user_view, name='follow_user'),
    path('transfer_book/', transfer_book_view, name='transfer_book'),
]