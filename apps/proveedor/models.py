from django.db import models

class proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    rubro = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre