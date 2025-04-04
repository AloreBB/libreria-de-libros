import os
import django
import datetime

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from libros.models import Libro

def crear_libros():
    libros = [
        {
            "titulo": "El Principito",
            "autor": "Antoine de Saint-Exupéry",
            "isbn": "978-3-16-148410-0",
            "fecha_publicacion": datetime.date(1943, 4, 6),
            "descripcion": "Un cuento poético y filosófico que explora temas universales.",
            "disponible": True
        },
        {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "isbn": "978-3-16-148410-1",
            "fecha_publicacion": datetime.date(1967, 5, 30),
            "descripcion": "Una saga familiar que mezcla realismo mágico con la historia de Macondo.",
            "disponible": True
        },
        {
            "titulo": "1984",
            "autor": "George Orwell",
            "isbn": "978-3-16-148410-2",
            "fecha_publicacion": datetime.date(1949, 6, 8),
            "descripcion": "Una distopía que advierte sobre el totalitarismo y la vigilancia masiva.",
            "disponible": True
        },
        {
            "titulo": "Don Quijote de la Mancha",
            "autor": "Miguel de Cervantes",
            "isbn": "978-3-16-148410-3",
            "fecha_publicacion": datetime.date(1605, 1, 16),
            "descripcion": "La obra cumbre de la literatura española.",
            "disponible": True
        },
        {
            "titulo": "Rayuela",
            "autor": "Julio Cortázar",
            "isbn": "978-3-16-148410-4",
            "fecha_publicacion": datetime.date(1963, 6, 28),
            "descripcion": "Una novela experimental que puede leerse en múltiples órdenes.",
            "disponible": True
        }
    ]

    for libro_data in libros:
        Libro.objects.get_or_create(**libro_data)
        print(f"Libro creado: {libro_data['titulo']}")

if __name__ == '__main__':
    print("Iniciando la población de la base de datos...")
    crear_libros()
    print("¡Población completada!")