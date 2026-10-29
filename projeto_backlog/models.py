from django.db import models
from django.db.models import Q

class Projeto(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome


class Backlog(models.Model):
    class Tipo(models.TextChoices):
        PRODUCT = "PRODUCT", "Product Backlog"
        SPRINT = "SPRINT", "Sprint Backlog"
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=Tipo.choices)
    data_criacao = models.DateField(auto_now_add= True)
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT, related_name="backlogs")

    class Meta:
        constraints = [
        models.UniqueConstraint(
            fields=["projeto"], condition=Q(tipo="PRODUCT"),
            name="um_produto_backlog_por_projeto"),
        ]
    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"