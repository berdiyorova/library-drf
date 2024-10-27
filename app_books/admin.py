from django.contrib import admin

from app_books.models import BookModel, AuthorModel

@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'first_name', 'last_name', 'email', 'bio')
    ordering = ('last_name',)


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isbn', 'author')
    search_fields = ('title', 'description', 'author')
    ordering = ('title',)
