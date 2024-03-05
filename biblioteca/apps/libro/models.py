from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=200, blank=False, null=False)
    apellidos = models.CharField(verbose_name='Apellido', max_length=220, blank=False, null=False)
    nacionalidad = models.CharField(verbose_name='Nacionalidad', max_length=100, blank=False, null=False)
    descripcion = models.TextField(verbose_name='Descripcion', blank=False, null=False)
    fecha_creacion = models.DateField(verbose_name='Fecha de creación', auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre