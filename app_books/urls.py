from django.urls import path

from app_books import views

app_name = 'books'

urlpatterns = [
    path('authors/', views.author_list_create_view, name='author_list_create'),
    path('', views.book_list_create_view, name='book_list_create'),
]
