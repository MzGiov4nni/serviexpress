from .models import empleado
from django import forms

class empleadoForm(forms.ModelForm):
    class Meta:
        model = empleado
        fields = (
            'rut',
            'nombre',
            'cargo'
        )
        labels = {
            'rut':'RUN',
            'nombre':'Nombre',
            'cargo':'Cargo'
        }
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'cargo':forms.TextInput(attrs={'class':'form-control'}),
        }