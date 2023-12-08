from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import servicio
from .forms import servicioForm
# Create your views here.

class servicioList (ListView):                    
    model = servicio
    template_name = 'servicio/servicio_list.html'

class servicioCreate (CreateView):
    model = servicio
    form_class = servicioForm
    template_name = 'servicio/servicio_form.html'
    success_url = reverse_lazy('servicio_list')

class servicioUpdate(UpdateView):
    model = servicio
    form_class = servicioForm
    template_name = 'servicio/servicio_form.html'
    success_url = reverse_lazy('servicio_list')

class servicioDelete(DeleteView):
    model = servicio
    template_name = 'servicio/servicio_borrar.html'
    success_url = reverse_lazy('servicio_list')
    
def servicios_disponibles(request):
    return render(request, 'servicio/serviciocliente_vista.html')