from django.urls import path

from app_books import views

app_name = 'books'

urlpatterns = [
    path('authors/<int:pk>', views.author_detail, name='author_detail'),
    path('<int:pk>', views.book_detail, name='book_detail'),
    path('authors', views.author_list_create_view, name='author_list_create'),
    path('', views.book_list_create_view, name='book_list_create'),
]
