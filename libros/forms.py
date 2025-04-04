from django import forms
from libros.models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'autor',
            'isbn',
            'fecha_publicacion',
            'descripcion',
            'disponible',
        ]
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }