from django.db import models

class empleado(models.Model):
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=45)
    cargo = models.CharField(max_length=50)

