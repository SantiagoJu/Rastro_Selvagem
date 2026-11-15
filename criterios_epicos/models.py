from django.db import models
from projeto_backlog.models import Projeto, Backlog
from django.conf import settings
from  decimal import Decimal

class Epico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    data_criacao = models.DateField(auto_now_add=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT, related_name= "epicos")

    def __str__(self):
        return self.nome

class HistoriaUsuario (models.Model):
    PONTOS = [(n, str(n)) 
              for n in (0,1,2,3,5,8,13,21,34,55)
    ]
    class MoSCoW (models.TextChoices):
        M = "M", "Must have"
        S = "S", "Should have"
        C = "C", "Could have"
        W = "W", "Won't have"

    class Impact(models.TextChoices):
        MASSIVO = "3", "Massivo (3)"
        ALTO = "2", "Alto (2)"
        MEDIO = "1", "Médio (1)"
        BAIXO = "0.5" "Baixo (0.5)"
        MINIMO = "0.25" "Mínimo (0.25)"

    class Confidence(models.IntegerChoices):
        ALTA = 100, "Alta (100%)"
        MEDIA = 80, "Média (80%)"
        BAIXA = 50, "Baixa (50%)"
  

    class Status (models.TextChoices):
        A_FAZER = "A_FAZER", "A fazer"
        EM_ANDAMENTO = "EM_ANDAMENTO", "Em andamento"
        EM_REVISAO = "EM_REVISAO", "Em revisão"
        CONCLUIDA = "CONCLUIDA", "Concluída"

        

    nome = models.CharField(max_length=100)
    acao = models.CharField(max_length=255)
    papel = models.CharField(max_length=255)
    data_criacao = models.DateField(auto_now_add=True)
    pontos_historia = models.PositiveSmallIntegerField(choices=PONTOS, default=1)
    moscow = models.CharField(max_length=1, choices=MoSCoW.choices)
    beneficio = models.CharField(max_length=255)

    rice_reach = models.PositiveIntegerField()
    rice_impact = models.CharField(max_length=18, choices= Impact.choices)
    rice_confidence = models.PositiveSmallIntegerField(choices=Confidence.choices)
    rice_effort = models.PositiveSmallIntegerField(choices=PONTOS)

    status = models.CharField(max_length= 13, choices=Status.choices, default=Status.A_FAZER)

    epico = models.ForeignKey(Epico, on_delete=models.SET_NULL,null=True, blank=True, related_name= "Historias")
    backlog = models.ForeignKey(Backlog, on_delete= models.PROTECT, related_name= "Historias")
    solicitante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.PROTECT, related_name= "Historias")

    @property
    def rice_scored(self):
        if self.rice_effort == 0:
            return None
        r = Decimal(self.rice_reach)
        i = Decimal(self.rice_impact)
        c = Decimal(self.rice_confidence) / 100
        e = Decimal(self.rice_effort)
        return (r*i*c)/e

    def __str__(self):
        return self.nome

class CriterioAceitacao(models.Model):
    contexto = models.CharField(max_length=255)
    evento = models.CharField(max_length=255)
    resultado = models.CharField(max_length=255)

    historia_usuario = models.ForeignKey(HistoriaUsuario, on_delete=models.CASCADE, related_name="Criterios")


