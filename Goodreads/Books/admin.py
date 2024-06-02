from django.contrib import admin
from .models import Author, Genre, BookSeries, Book, Review, Follow, Comment, Like, ActivityLog, Shelf

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookSeries)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(ActivityLog)
admin.site.register(Shelf)