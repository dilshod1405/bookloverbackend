from django.urls import path, include
from .views import BooksListView, BookDetailsView, CategoryListView, BookReadCountsView, count_books_by_category_type
from rest_framework import routers



urlpatterns = [
    path('all_books/', BooksListView.as_view({'get': 'list'}), name='book_list'),
    path('books/<int:pk>/', BookDetailsView.as_view(), name='book_view'),
    path('book/<int:pk>/', BookReadCountsView.as_view(), name='book_read_count'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('count_books/', count_books_by_category_type, name='count-books-by-category'),
]