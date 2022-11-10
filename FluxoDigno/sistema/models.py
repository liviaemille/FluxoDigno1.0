from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


def validate_number(value):
    if not value.isdigit():
        raise ValidationError('O valor indicado deve conter apenas números') 

class pontosColeta(models.Model):
    nome = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10, validators=[validate_number])
    descricao = models.CharField(max_length=100, null=False)
    pix = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=11, null=True, blank=True, default=None, validators=[validate_number])
    horaabertura = models.TimeField(auto_now=False, auto_now_add=False, default="00:00")
    horafechamento = models.TimeField(auto_now=False, auto_now_add=False, default="00:00")

    def __str__(self):
        return self.nome

class Doacoes(models.Model):
    produto = models.CharField(max_length=50)
    doador = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    pontocoleta = models.ForeignKey(pontosColeta, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto