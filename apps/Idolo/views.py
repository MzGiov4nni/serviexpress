from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Idolo
from .forms import IdoloForm
# Create your views here.

class IdoloList (ListView):                    
    model = Idolo
    template_name = 'Idolo/idolo_list.html'

class IdoloCreate (CreateView):
    model = Idolo
    form_class = IdoloForm
    template_name = 'Idolo/idolo_form.html'
    success_url = reverse_lazy('idolo_list')

class IdoloUpdate(UpdateView):
    model = Idolo
    form_class = IdoloForm
    template_name = 'Idolo/idolo_form.html'
    success_url = reverse_lazy('idolo_list')

class IdoloDelete(DeleteView):
    model = Idolo
    template_name = 'Idolo/idolo_borrar.html'
    success_url = reverse_lazy('idolo_list')


def consulta_cocktail_view(request):
    return render(request, 'CocktailApi/consulta_cocktail.html')

def buscar_cocktail_view(request):
    return render(request, 'CocktailApi/buscar_cocktail.html')

def contacto_view(request):
    return render(request, 'Usuario/Contacto.html')

