from django.shortcuts import render
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Projeto, Backlog

# Views do Projeto

class ProjetoListView(LoginRequiredMixin, ListView):
    model = Projeto
    template_name = 'projeto_backlog/projeto_list.html'
    context_object_name = 'projetos'

class ProjetoCreateView(LoginRequiredMixin, CreateView):
    model = Projeto
    template_name = 'projeto_backlog/projeto_form.html'
    fields = ['nome']
    success_url = reverse_lazy('projeto_backlog:projeto_list')

class ProjetoUpdateView(LoginRequiredMixin, UpdateView):
    model = Projeto
    template_name = 'projeto_backlog/projeto_form.html'
    fields = ['nome']
    success_url = reverse_lazy('projeto_backlog:projeto_list')

class ProjetoDeleteView(LoginRequiredMixin, DeleteView):
    model= Projeto
    template_name = 'projeto_backlog/projeto_confirm_delete.html'
    success_url = reverse_lazy('projeto_backlog:projeto_list')

class ProjetoDatailView(LoginRequiredMixin, DetailView):
    model = Projeto
    template_name = 'projeto_backlog/projeto_detail.html'
    context_object_name = 'projeto'


#Views do BackLog

class BacklogListView(LoginRequiredMixin, ListView):
    model = Backlog 
    template_name = 'projeto_backlog/backlog_list.html'
    context_object_name = 'backlogs'

class BacklogCreateView(CreateView):
    model = Backlog
    template_name = 'projeto_backlog/backlog_form.html'
    fields = ['nome', 'tipo', 'projeto']
    success_url = reverse_lazy('projeto_backlog:backlog_list')

class BacklogUpdateView(LoginRequiredMixin, UpdateView):
    model = Backlog
    template_name = 'projeto_backlog/backlog_form.html'
    fields = ['nome', 'tipo', 'projeto']
    success_url = reverse_lazy('projeto_backlog:backlog_list')

class BacklogDeleteView(LoginRequiredMixin, DeleteView):
    model = Backlog
    template_name = 'projeto_backlog/backlog_confirm_delete.html'
    success_url = reverse_lazy('projeto_backlog:backlog_list')
              