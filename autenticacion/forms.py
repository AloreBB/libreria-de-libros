from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    document_id = forms.CharField(
        max_length=20,
        required=True,
        label="Documento de Identidad",
        help_text="Ingrese su documento de identidad.",
    )
    age = forms.IntegerField(
        required=True, min_value=1, label="Edad", help_text="Ingrese su edad."
    )

    class Meta:
        model = Usuario
        fields = ("username", "password1", "password2", "age", "document_id", "email")

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ("username", "password")
