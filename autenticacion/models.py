from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """
    Modelo de usuario personalizado que extiende el AbstractUser de Django.
    Puedes agregar campos adicionales según necesites.
    """

    email = models.EmailField(unique=True)
    document_id = models.CharField(
        max_length=20, unique=True, verbose_name="Documento de Identidad"
    )
    age = models.PositiveIntegerField("Edad")

    def __str__(self):
        return self.username
