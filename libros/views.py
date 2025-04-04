from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q

from libros.models import Libro
from libros.forms import LibroForm

# Create your views here.
TEMPLATE_DEVOLVER = "libros/devolver.html"


def listado(request):
    query = request.GET.get('q', '')
    queryset = Libro.objects.all()
    
    if query:
        queryset = queryset.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(isbn__icontains=query)
        )
    
    return render(request, "libros/listado.html", {
        "libros": queryset,
        "query": query
    })


def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    return render(request, "libros/detalle.html", {"libro": libro})


def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            messages.success(request, f"Libro '{libro.titulo}' creado correctamente")
            return redirect("listado")
    else:
        form = LibroForm()

    return render(
        request, "libros/formulario.html", {"form": form, "titulo": "Nuevo Libro"}
    )


def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Libro '{libro.titulo}' actualizado correctamente"
            )
            return redirect("listado")
    else:
        form = LibroForm(instance=libro)

    return render(
        request,
        "libros/formulario.html",
        {"form": form, "titulo": f"Editar Libro: {libro.titulo}"},
    )


def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == "POST":
        titulo = libro.titulo
        libro.delete()
        messages.success(request, f"Libro '{titulo}' eliminado correctamente")
        return redirect("listado")

    return render(request, "libros/confirmar_eliminar.html", {"libro": libro})


def prestar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == "POST":
        if libro.disponible:
            libro.disponible = False
            libro.save()
            messages.success(request, f"Libro '{libro.titulo}' prestado correctamente")
        else:
            messages.error(
                request, f"El libro '{libro.titulo}' no está disponible para préstamo"
            )
        return redirect("listado")

    return render(request, "libros/confirmar_prestamo.html", {"libro": libro})


def devolver_libro(request, pk=None):
    if pk:
        libro = get_object_or_404(Libro, pk=pk)

        if request.method == "POST":
            libro.disponible = True
            libro.save()
            messages.success(request, "El libro ha sido devuelto exitosamente.")
            return redirect("listado")
        return render(request, TEMPLATE_DEVOLVER, {"libro": libro})

    query = request.GET.get("query", "")
    if query:
        libros = Libro.objects.filter(
            Q(titulo__icontains=query)
            | Q(autor__icontains=query)
            | Q(descripcion__icontains=query)
            | Q(id__icontains=query)
        ).filter(disponible=True)
        return render(request, TEMPLATE_DEVOLVER, {"libros": libros, "query": query})
    return render(request, TEMPLATE_DEVOLVER)
