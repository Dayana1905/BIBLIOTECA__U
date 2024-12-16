from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Libro, Usuario, Prestamo

def lista_libros(request):
    libros = list(Libro.objects.all().values())
    return JsonResponse(libros, safe=False)

def lista_usuarios(request):
    usuarios = list(Usuario.objects.all().values())
    return JsonResponse(usuarios, safe=False)

def lista_prestamos(request):
    prestamos = list(Prestamo.objects.all().values())
    return JsonResponse(prestamos, safe=False)