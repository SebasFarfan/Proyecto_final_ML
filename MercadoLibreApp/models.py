from django.db import models

# Create your models here.

class Producto_encontrado(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.FloatField()
    url=models.CharField(max_length=300)
    imagen=models.CharField(max_length=300)


class Nombre_producto(models.Model):
    nombre=models.CharField(max_length=100)


