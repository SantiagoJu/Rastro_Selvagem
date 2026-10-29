from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    class Papel(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        GESTOR = "GESTOR", "Gestor"
        VOLUNTARIO = "VOLUNTARIO", "Voluntario"

    papel = models.CharField(max_length=30, choices=Papel.choices, default=Papel.VOLUNTARIO)
    data_saida = models.DateField(null=True, blank=True)
