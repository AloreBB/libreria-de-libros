from django.shortcuts import render

from libros.models import Libro

# Create your views here.


def listado(request):
    queryset = Libro.objects.all()
    return render(request, "libros/listado.html", {"libros": queryset})
