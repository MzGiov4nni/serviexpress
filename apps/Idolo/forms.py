from .models import Idolo
from django import forms

class IdoloForm(forms.ModelForm):
    class Meta:
        model = Idolo
        fields = (
            'fotografia',
            'rut',
            'nombre'
        )
        labels = {
            'fotografia':'Fotografia',
            'rut':'RUN',
            'nombre':'Nombre'
        }
        widgets = {
            #'fotografia':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
        }