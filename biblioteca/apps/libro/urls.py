from django.urls import path, re_path
from .views import crearAutor, listarAutor 

urlpatterns =  [
    path('crear_autor/', crearAutor, name='crear_autor'),
    path('listar_autor/',listarAutor, name='listar_autor')

    re_path(r'^crear_autor/(?P<id>\d+)', crearAutor, name="csskf")
]