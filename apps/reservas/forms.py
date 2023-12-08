from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_hora_reserva']
        widgets = {
            'fecha_hora_reserva': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }