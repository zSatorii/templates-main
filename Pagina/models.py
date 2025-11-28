from django.db import models
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField
    cantidad = models.IntegerField
    hay = models.BooleanField

    def __str__(self):
        return self.nombre
# Create your models here.
