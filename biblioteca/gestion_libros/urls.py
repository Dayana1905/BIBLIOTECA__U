from django.urls import path
from .views import lista_libros, lista_usuarios, lista_prestamos

urlpatterns = [
    path('api/libros/', lista_libros, name='lista_libros'),
    path('api/usuarios/', lista_usuarios, name='lista_usuarios'),
    path('api/prestamos/', lista_prestamos, name='lista_prestamos'),
]
