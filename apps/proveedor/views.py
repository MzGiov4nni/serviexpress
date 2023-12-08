from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import proveedor
from .forms import proveedorForm
# Create your views here.

class proveedorList (ListView):                    
    model = proveedor
    template_name = 'proveedor/proveedor_list.html'

class proveedorCreate (CreateView):
    model = proveedor
    form_class = proveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')

class proveedorUpdate(UpdateView):
    model = proveedor
    form_class = proveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')

class proveedorDelete(DeleteView):
    model = proveedor
    template_name = 'proveedor/proveedor_borrar.html'
    success_url = reverse_lazy('proveedor_list')