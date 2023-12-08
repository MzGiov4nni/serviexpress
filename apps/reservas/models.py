from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_hora_reserva = models.DateTimeField()

    def __str__(self):
        return f"Reserva para {self.usuario.username} - {self.fecha_hora_reserva}"