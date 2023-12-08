from .models import proveedor
from django import forms

class proveedorForm(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = (
            'nombre',
            'contacto',
            'rubro'
        )
        labels = {
            'nombre':'Nombre',
            'contacto':'Contacto',
            'rubro':'Rubro'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'contacto':forms.TextInput(attrs={'class':'form-control'}),
            'rubro':forms.TextInput(attrs={'class':'form-control'}),
        }