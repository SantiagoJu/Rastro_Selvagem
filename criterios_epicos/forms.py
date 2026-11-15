from django import forms
from django.forms import inlineformset_factory

from .models import CriterioAceitacao, HistoriaUsuario

class HistoriaUsuarioForm(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = [
            "nome", "papel", "acao",
            "beneficio",
            "backlog", "epico",
            "pontos_historia", "moscow",
            "rice_reach", "rice_impact", "rice_confidence", "rice_effort",
        ]
        widgets = {
            "rice_reach": forms.NumberInput(attrs={"min": 0, "step": 10}),
            # rice_effort continua como select: o requisito manda usar os valores dos pontos de história.
        }

    def __init__(self, *args, projeto, **kwargs):
        super().__init__(*args, **kwargs)
        # Backlog e épico só do projeto atual
        self.fields["backlog"].queryset = projeto.backlogs.all()
        self.fields["epico"].queryset = projeto.epicos.all()
        # O Figma marca o épico como obrigatório (no model ele aceita null)
        self.fields["epico"].required = True
        self.fields["epico"].empty_label = "Selecione um épico"


# Uma linha de critério = Dado (contexto) / Quando (evento) / Então (resultado).
# extra=1 e min_num=1: na criação aparecem 2 linhas, a primeira obrigatória.
# Use min_num=0 e validate_min=False se a história puder ficar sem critérios.
CriterioFormSet = inlineformset_factory(
    HistoriaUsuario,
    CriterioAceitacao,
    fields=("contexto", "evento", "resultado"),
    extra=1,
    min_num=1,
    validate_min=True,
    can_delete=True,
    widgets={
        "contexto": forms.TextInput(attrs={"placeholder": "um resgate em atendimento"}),
        "evento": forms.TextInput(attrs={"placeholder": "registro os dados do animal"}),
        "resultado": forms.TextInput(attrs={"placeholder": "a entrada fica disponível na triagem"}),
    },
)