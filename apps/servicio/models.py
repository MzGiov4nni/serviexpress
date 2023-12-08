from django.db import models

class servicio(models.Model):
    nombre= models.CharField(max_length=100)
    tipo= models.CharField(max_length=100)
