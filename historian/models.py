from django.db import models

# Create your models here.

class Personaje(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=True, verbose_name='Nombre')
    apellido = models.CharField(max_length=200, null=False, blank=True, verbose_name='Apellido')
    pais_de_origen = models.CharField(max_length=100, null=False, blank=True, verbose_name='País de Origen')
    fecha_de_nacimiento = models.DateField(null=False, blank=True, verbose_name='Fecha de Nacimiento')
    fecha_de_muerte = models.DateField(null=True, blank=True, verbose_name='Fecha de Muerte')
    biografia = models.TextField(null=True, blank=True, verbose_name='Biografía')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Personaje"
        verbose_name_plural = "Personajes"


class Hecho_Historico(models.Model):
    personajes = models.ManyToManyField(Personaje)
    nombre = models.CharField(max_length=100, null=False, blank=True, verbose_name='Nombre')
    fecha = models.DateField(null=False, blank=True, verbose_name='Fecha')
    resumen = models.TextField(null=True, blank=True, verbose_name='Resumen')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')
    palabras_clave_1 = models.TextField(null=True, blank=True, verbose_name='Palabra Clave 1')
    palabras_clave_2 = models.TextField(null=True, blank=True, verbose_name='Palabra Clave 2')
    palabras_clave_3 = models.TextField(null=True, blank=True, verbose_name='Palabra Clave 3')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Hecho Histórico"
        verbose_name_plural = "Hechos Históricos"
    
