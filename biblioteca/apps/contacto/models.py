from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(blank=True, max_length=100, verbose_name='Nombre')
    apellido = models.CharField(blank=True, max_length=100, verbose_name='Apellido')
    correo = models.EmailField(unique=True, max_length=100, verbose_name='Correo')
    edad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'