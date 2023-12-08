from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import empleado
from .forms import empleadoForm
# Create your views here.

class empleadoList (ListView):                    
    model = empleado
    template_name = 'empleado/empleado_list.html'

class empleadoCreate (CreateView):
    model = empleado
    form_class = empleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class empleadoUpdate(UpdateView):
    model = empleado
    form_class = empleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class empleadoDelete(DeleteView):
    model = empleado
    template_name = 'empleado/empleado_borrar.html'
    success_url = reverse_lazy('empleado_list')