from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from servicii.forms import ServiciiForm
from servicii.models import ServiciiModel


# Create your views here.


class ServiciiDetailsView(DetailView):
    template_name = 'servicii/detalii.html'
    model = ServiciiModel  #select * from ServiciiModel where id=pk


class ServiciiListView(ListView):
    template_name = 'servicii/all.html'
    model = ServiciiModel


class ServiciiUpdateView(UpdateView): #pentru update in baza de date
    form_class = ServiciiForm
    template_name = 'create_update_form.html'
    model = ServiciiModel
    success_url = reverse_lazy('serviciu-all')


class ServiciiDeleteView(DeleteView):
    template_name = 'delete_form.html'
    model = ServiciiModel
    success_message = "Serviciu sters cu succes"
    success_url = reverse_lazy('serviciu-all')


class ServiciiCreateView(CreateView): #pentru insert in baza de date
    form_class = ServiciiForm
    template_name = 'create_update_form.html'
    model = ServiciiModel
    success_url = reverse_lazy('serviciu-all')