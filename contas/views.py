from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','email','papel']

class CadastroView(CreateView):
    form_class = UsuarioCreationForm
    template_name ='contas/cadastro.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'contas/login.html'
    redirect_authenticated_user = True
    
