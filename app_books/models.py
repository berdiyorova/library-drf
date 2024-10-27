from django.db import models

class AuthorModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    bio = models.TextField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class BookModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=17, unique=True)
    cover_picture = models.ImageField(default='book_cover.png', upload_to='books/')

    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
