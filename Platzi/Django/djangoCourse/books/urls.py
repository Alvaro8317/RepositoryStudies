from django.urls import path
from .views import get_books

urlpatterns = [
    path('listar-libros/', get_books, name='listar_libros'),
]
