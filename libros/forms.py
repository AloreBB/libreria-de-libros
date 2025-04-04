from django import forms
from libros.models import Libro


class LibroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Libro
        fields = [
            "titulo",
            "autor",
            "isbn",
            "fecha_publicacion",
            "descripcion",
            "disponible",
        ]
        widgets = {
            "fecha_publicacion": forms.DateInput(attrs={"type": "date"}),
            "descripcion": forms.Textarea(attrs={"rows": 4}),
        }
