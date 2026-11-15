from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy, reverse
from .models import Epico, CriterioAceitacao, HistoriaUsuario
from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from projeto_backlog.models import Backlog, Projeto
from .forms import CriterioFormSet, HistoriaUsuarioForm
from .models import HistoriaUsuario
from django.http import JsonResponse
from django.views import View

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

class HistoriaFormMixin(LoginRequiredMixin):
    """Cuida da história e dos critérios juntos, em uma única transação."""

    model = HistoriaUsuario
    form_class = HistoriaUsuarioForm
    template_name = "criterios_epicos/historia_form.html"

    def get_projeto(self):
        raise NotImplementedError

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["projeto"] = self.get_projeto()
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["projeto"] = self.get_projeto()
        if "formset" not in ctx:
            # self.object é None na criação, e o formset cria uma instância vazia
            ctx["formset"] = CriterioFormSet(instance=self.object)
        return ctx

    def form_invalid(self, form):
        # A história tem erro: devolve também o que foi digitado nos critérios
        formset = CriterioFormSet(self.request.POST, instance=self.object)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def form_valid(self, form):
        formset = CriterioFormSet(self.request.POST, instance=form.instance)
        if not formset.is_valid():
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

        with transaction.atomic():
            if not form.instance.pk:
                form.instance.solicitante = self.request.user
            self.object = form.save()
            formset.instance = self.object
            formset.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse("criterios_epicos:historia_detail", args=[self.object.pk])


class HistoriaCreateView(HistoriaFormMixin, CreateView):
    """Abra com ?projeto=<pk> e, opcionalmente, &backlog=<pk>."""

    def get_projeto(self):
        if not hasattr(self, "_projeto"):
            projeto_id = self.request.GET.get("projeto", "")
            backlog_id = self.request.GET.get("backlog", "")
            if projeto_id.isdigit():
                self._projeto = get_object_or_404(Projeto, pk=projeto_id)
            elif backlog_id.isdigit():
                self._projeto = get_object_or_404(Backlog, pk=backlog_id).projeto
            else:
                raise Http404("Informe o projeto da nova história.")
        return self._projeto

    def get_initial(self):
        initial = super().get_initial()
        backlog_id = self.request.GET.get("backlog", "")
        if backlog_id.isdigit():
            initial["backlog"] = backlog_id
        return initial


class HistoriaUpdateView(HistoriaFormMixin, UpdateView):
    def get_projeto(self):
        return self.object.backlog.projeto

class HistoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = HistoriaUsuario
    template_name = "criterios_epicos/historiausuario_confirm_delete.html"

    def get_success_url(self):
        # O Django chama este método antes de apagar, então self.object ainda existe.
        return reverse("criterios_epicos:historia_kanban", args=[self.object.backlog.projeto_id])

class HistoriasDoProjetoMixin(LoginRequiredMixin):
    """Escopo compartilhado pelo backlog em lista e pelo Kanban.

    Descobre o projeto (pela URL), o backlog e o épico escolhidos (pela query string)
    e devolve as histórias já filtradas. Assim as duas telas nunca divergem.
    """

    def carregar_escopo(self):
        # Aqui entra a regra "somente projetos vinculados à sua conta".
        self.projeto = get_object_or_404(Projeto, pk=self.kwargs["projeto_pk"])

        backlogs = self.projeto.backlogs.all()
        backlog_id = self.request.GET.get("backlog")
        self.backlog = (
            (backlogs.filter(pk=backlog_id).first() if backlog_id else None)
            or backlogs.filter(tipo="PRODUCT").first()
            or backlogs.first()
        )

        epico_id = self.request.GET.get("epico")
        self.epico = self.projeto.epicos.filter(pk=epico_id).first() if epico_id else None

    def historias(self):
        qs = (
            HistoriaUsuario.objects
            .filter(backlog=self.backlog)
            .select_related("epico", "solicitante")
        )
        if self.epico:
            qs = qs.filter(epico=self.epico)
        return qs

class KanbanView(HistoriasDoProjetoMixin, TemplateView):
    template_name = "criterios_epicos/historia_kanban.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        self.carregar_escopo()

        # rice_scored é uma property, então a ordenação por RICE é feita em Python.
        historias = sorted(self.historias(), key=lambda h: h.rice_scored or 0, reverse=True)

        # Uma coluna por status, mesmo as vazias, na ordem definida no model.
        colunas = [
            {
                "valor": valor,
                "rotulo": rotulo,
                "historias": [h for h in historias if h.status == valor],
            }
            for valor, rotulo in HistoriaUsuario.Status.choices
        ]

        ctx.update(
            projeto=self.projeto,
            backlog_atual=self.backlog,
            epico_atual=self.epico,
            colunas=colunas,
        )
        return ctx

class HistoriaStatusView(LoginRequiredMixin, View):
    """Muda só o status. Serve o arrastar do Kanban (fetch) e o seletor do detalhe (form)."""

    http_method_names = ["post"]

    def post(self, request, pk):
        # Aqui também vale checar se o usuário pertence ao projeto da história.
        historia = get_object_or_404(HistoriaUsuario, pk=pk)

        novo = request.POST.get("status")
        if novo not in HistoriaUsuario.Status.values:
            return JsonResponse({"ok": False, "erro": "Status inválido."}, status=400)

        historia.status = novo
        historia.save(update_fields=["status"])

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"ok": True, "status": novo})
        return redirect("criterios_epicos:historia_detail", pk=historia.pk)

class HistoriaListView(HistoriasDoProjetoMixin, TemplateView):
    template_name = "criterios_epicos/historia_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        self.carregar_escopo()
        historias = sorted(self.historias(), key=lambda h: h.rice_scored or 0, reverse=True)
        ctx.update(projeto=self.projeto, backlog_atual=self.backlog, historias=historias)
        return ctx

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
