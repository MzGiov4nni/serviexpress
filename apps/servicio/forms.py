from .models import servicio
from django import forms

class servicioForm(forms.ModelForm):
    class Meta:
        model = servicio
        fields = (
            'nombre',
            'tipo'
        )
        labels = {
            'nombre':'Nombre',
            'tipo':'Tipo'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.TextInput(attrs={'class':'form-control'}),
        }