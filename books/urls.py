from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('ordered_books/', views.ordered_books, name='ordered_books'),
]