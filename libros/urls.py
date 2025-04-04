from django.urls import path
from libros import views

urlpatterns = [
    path('', views.listado, name='listado'),
    path('libro/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('libro/nuevo/', views.crear_libro, name='crear_libro'),
    path('libro/<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),
    path('libro/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
    path('libro/<int:libro_id>/prestar/', views.prestar_libro, name='prestar_libro'),
    path('devolver/', views.devolver_libro, name='devolver_buscar'),
    path('devolver/<int:pk>/', views.devolver_libro, name='devolver_libro'),
]
