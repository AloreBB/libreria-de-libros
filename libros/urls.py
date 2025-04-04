from django.urls import path
from . import views

urlpatterns = [
    path("listado/", views.listado, name="libros-list"),
]
