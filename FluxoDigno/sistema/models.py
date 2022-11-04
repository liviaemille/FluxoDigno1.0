from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


"""def validacao_cpf(cpf):
    if not cpf.isdigit():
        raise ValidationError('O CPF deve conter apenas números')

class usuarioDoador(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True, validators=[validacao_cpf, MinLengthValidator(11)])
    email = models.EmailField()
    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

"""
class pontosColeta(models.Model):
    nome = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100, null=False)
    pix = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=11)
    horaAbertura = models.TimeField(auto_now=False, auto_now_add=False, default="00:00")
    horaFechamento = models.TimeField(auto_now=False, auto_now_add=False, default="00:00")

    def __str__(self):
        return self.nome

class Doacoes(models.Model):
    produto = models.CharField(max_length=50)
   # doador = models.ForeignKey(, on_delete=models.CASCADE)
    data = models.DateField()
    pontocoleta = models.ForeignKey("pontosColeta", on_delete=models.CASCADE)

    def __str__(self):
        return self.produto