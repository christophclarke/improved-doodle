from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('monsters', views.monster_list, name='monster_list'),
    path('monster/<int:monster_id>', views.monster_detail, name='monster_detail'),
    path('authors', views.authors_list, name='author_list'),
    path('author/<int:author_id>', views.author_detail, name='author_detail'),
    path('books', views.books_list, name='book_list'),
    path('book/<int:book_id>', views.book_detail, name='book_detail'),
    path('theses', views.theses_list, name='thesis_list'),
    path('thesis/<int:thesis_id>', views.thesis_detail, name='thesis_detail'),
    path('thesis/comparison', views.thesis_comparison, name='thesis_comparison'),
]
