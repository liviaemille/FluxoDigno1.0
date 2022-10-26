from django.db import models

# Create your models here.
class pontosColeta(models.Model):
    nome = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100, null=False)
    pix = models.CharField(max_length=100, null=False)
   # horaAbertura = models.