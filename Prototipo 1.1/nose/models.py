from django.db import models

# Create your models here.

class Camionero(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, verbose_name='Cédula')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    autonomo = models.BooleanField(default=True, verbose_name='Autónomo')

    @property
    def autonomo_texto(self):
        return "Sí" if self.autonomo else "No"

    def __str__(self):
        return f"Cédula: {self.cedula} - Nombre: {self.nombre} - Apellido: {self.apellido} - Autónomo: {self.autonomo_texto}"

class Camion(models.Model):
    placa = models.CharField(primary_key=True, max_length=10, verbose_name='Placa')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    alto = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Alto')
    ancho = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ancho')
    largo = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Largo')

    def __str__(self):
        return f"Placa: {self.placa} - Modelo: {self.modelo} - Dimensiones: {self.alto} x {self.ancho} x {self.largo}"
