from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Epico, CriterioAceitacao, HistoriaUsuario

# CRUD EPICO

class EpicoListView(LoginRequiredMixin, ListView):
    model = Epico
    template_name = 'criterios_epicos/epico_list.html'
    context_object_name = 'epicos'

class EpicoCreateView (LoginRequiredMixin, CreateView):
    model = Epico
    template_name = 'criterios_epicos/epico_form.html'
    fields = ['nome', 'descricao', 'projeto']
    success_url = reverse_lazy('criterios_epicos:epico_list')

class EpicoUpdateView(LoginRequiredMixin, UpdateView):
    model = Epico
    template_name = 'criterios_epicos/epico_form.html'
    fields = ['nome', 'descricao', 'projeto']
    success_url = reverse_lazy('criterios_epicos:epico_list')

class EpicoDeleteView(LoginRequiredMixin, DeleteView):
    model = Epico
    template_name = 'criterios_epicos/epico_confirm_delete.html'
    success_url = reverse_lazy('criterios_epicos:epico_list')

class EpicoDetailView(LoginRequiredMixin, DetailView):
    model = Epico
    template_name = 'criterios_epicos/epico_detail.html'
    context_object_name = 'epico'


#CRUD HISTÓRIAS DE USUÁRIO

class HistoriaUsuarioListView(LoginRequiredMixin, ListView):
    model = HistoriaUsuario
    template_name= 'criterios_epicos/historia_list.html'
    context_object_name = 'historias'

class HistoriaUsuarioCreateView(LoginRequiredMixin, CreateView):
    model = HistoriaUsuario
    template_name = 'criterios_epicos/historia_form.html'
    fields= ['nome','acao','papel','pontos_historia', 'moscow','rice_reach','rice_impact', 'rice_confidence', 'rice_effort', 'epico', 'backlog','solicitante']
    success_url = reverse_lazy('criterios_epicos:historia_list')

class HistoriaUsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = HistoriaUsuario
    template_name = 'criterios_epicos/historia_form.html'
    fields = ['nome','acao','papel','pontos_historia', 'moscow','rice_reach','rice_impact', 'rice_confidence', 'rice_effort', 'status', 'epico', 'backlog','solicitante']
    success_url = reverse_lazy('criterios_epicos:historia_list')

class HistoriaUsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = HistoriaUsuario
    template_name = 'criterios_epicos/historia_confirm_delete.html'
    success_url = reverse_lazy('criterios_epicos:historia_list')

class HistoriaUsuarioDetailView(LoginRequiredMixin, DetailView):
    model = HistoriaUsuario
    template_name = 'criterios_epicos/historia_detail.html'
    context_object_name = 'historia'


#CRUD CRITERIOS DE ACEITAÇÃO

class CriterioListView(LoginRequiredMixin, ListView):
    model = CriterioAceitacao
    template_name = 'criterios_epicos/criterio_list.html'
    context_object_name = 'criterios'

class CriterioCreateView(LoginRequiredMixin, CreateView):
    model = CriterioAceitacao
    template_name = 'criterios_epicos/criterio_form.html'
    fields = ['contexto','evento','resultado','historia_usuario']
    success_url = reverse_lazy('criterios_epicos:criterio_list')

class CriterioUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterioAceitacao
    template_name = 'criterios_epicos/criterio_form.html'
    fields = ['contexto','evento','resultado','historia_usuario']
    success_url = reverse_lazy('criterios_epicos:criterio_list')

class CriterioDeleteView(LoginRequiredMixin, DeleteView):
    model = CriterioAceitacao
    template_name = 'criterios_epicos/criterio_confirm_delete.html'
    success_url = reverse_lazy('criterios_epicos:criterio_list')

class CriterioDetailView(LoginRequiredMixin, DetailView):
    model = CriterioAceitacao
    template_name = 'criterios_epicos/criterio_detail.html'
    context_object_name = 'criterio'
