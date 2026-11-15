from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Projeto, Backlog
from django.db.models import Count, Sum
# Views do Projeto

class ProjetoListView(LoginRequiredMixin, ListView):
    model = Projeto
    template_name = 'projeto_backlog/projeto_list.html'
    context_object_name = 'projetos'
    def get_queryset(self):
        return (
            Projeto.objects
            .annotate(
                total_backlogs=Count("backlogs", distinct=True),
                total_historias=Count("backlogs__Historias", distinct=True),
                total_pontos=Sum("backlogs__Historias__pontos_historia"),
            )
            .order_by("pk")
        )

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

class BacklogCreateView(LoginRequiredMixin, CreateView):
    model = Backlog
    template_name = 'projeto_backlog/backlog_form.html'
    fields = ['nome', 'tipo', 'projeto']
    def get_initial(self):
        initial = super().get_initial()
        projeto_id = self.request.GET.get("projetos")
        if projeto_id:
            initial["projeto"] = projeto_id
        return initial

    def get_success_url(self):
        return reverse("projeto_backlog:projeto_detail", args=[self.object.projeto.pk])

class BacklogUpdateView(LoginRequiredMixin, UpdateView):
    model = Backlog
    template_name = 'projeto_backlog/backlog_form.html'
    fields = ['nome', 'tipo', 'projeto']
    def get_success_url(self):
            return reverse("projeto_backlog:projeto_detail", args=[self.object.projeto.pk])

class BacklogDeleteView(LoginRequiredMixin, DeleteView):
    model = Backlog
    template_name = 'projeto_backlog/backlog_confirm_delete.html'
    #success_url = reverse_lazy('projeto_backlog:backlog_list')
    def get_success_url(self):
            return reverse("projeto_backlog:projeto_detail", args=[self.object.projeto.pk])          