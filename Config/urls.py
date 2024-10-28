from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('app_books.urls', namespace='books')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
