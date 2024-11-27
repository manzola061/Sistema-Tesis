from django.db import models

# Create your models here.

class Camionero(models.Model):
    cedula = models.CharField(primary_key=True, max_length=100, verbose_name='Cédula')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    autonomo = models.BooleanField(default=True, verbose_name='Autónomo')

    @property
    def autonomo_texto(self):
        return "Sí" if self.autonomo else "No"

    def __str__(self):
        fila = "Cédula: " + self.cedula + " - " + "Nombre: " + self.nombre + " - " + "Apellido: " + self.apellido + " - " + "Autónomo: " + self.autonomo_texto
        return fila