from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE, blank=True, null=True)

class Endereco(models.Model):
    cep = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=200)
