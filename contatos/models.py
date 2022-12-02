from django.db import models

# Create your models here.

class Contatos(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    contato_de_Emergência = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)