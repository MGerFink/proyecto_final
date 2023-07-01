from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.list import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView

from .models import Usuario

# Create your views here.


class UsuariosBaseView(View):
    template_name = "usuarios.html"
    model = Usuario
    fields = '__al__'
    success_url = reverse_lazy('usuarios:all')

class UsuariosListView(UsuariosBaseView, ListView):
    """
    ESTO ME PERMITE CREAR UNA LISTA CON LOS USUARIOS
    """

class UsuariosDetailView(UsuariosBaseView, DetailView):
    template_name = "usuario_detail.html"


class UsuariosCreateView(UsuariosBaseView, CreateView):
    template_name = "usuario_create.html"
    extra_context = {
        "tipo": "Crear usuario"
    }    

class UsuariosUpdateView(UsuariosBaseView, UpdateView):
    template_name = "usuario_update.html"
    extra_context = {
        "tipo": "Actualizar usuario"
    }

class UsuariosDeleteView(UpdateView, DeleteView):
    template_name = "usuario_delete.html"
    extra_context = {
        "tipo": "Borrar usuario"
    }
