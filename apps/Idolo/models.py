from django.db import models

class Idolo(models.Model):
    fotografia = models.ImageField(upload_to='idolos')
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.fotografia)
