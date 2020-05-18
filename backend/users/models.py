from django.db import models
from django.contrib.auth.models import User

TYPE_USER = [
    ("medico", "Médico(a)"),
    ("pesquisador", "Pesquisador(a)")
]

class CustomUser(models.Model):
    name = models.CharField("Nome", max_length=30, null=True)
    register = models.CharField("Nº de registro", max_length=15, null=True)
    email = models.EmailField("E-mail", null=True)
    approved = models.BooleanField("Aprovado(a)", default=False, blank=False, null=True)
    type = models.CharField("Tipo", max_length=20, choices=TYPE_USER, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
