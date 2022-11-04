from django.shortcuts import render, redirect
from .forms import DoacoesForm
from .models import Doacoes, pontosColeta


def tela_inicio (request):
    return render(request, "../templates/sistema/index.html")

def nova_doacao(request):
    form = DoacoesForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_doacoes')
    return render(request, '../templates/sistema/form_doacao.html', {'form': form})

def ver_doacoes(request):
    doacoes = Doacoes.objects.all()
    return render (request, '../templates/sistema/doacoes.html', {'doacoes': doacoes})

def editar_doacao(request):
    doacao = Doacoes.objects.get(id=id)
    form = DoacoesForm(request.POST or None, instance=doacao)

    if form.is_valid():
        form.save()
        return redirect('ver_doacoes')

    return render(request, '../templates/sistema/doacoes.html', {'form': form, 'doacao': doacao})

def ver_pontoscoleta(request):
    pontos = pontosColeta.objects.all()
    return render (request, '../templates/sistema/pontoscoleta.html', {"pontos": pontos})


"""def cadastro (request):
    if request.method == 'GET':
        return render (request, 'cadastro.html')
    else :
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username==username).first()

        if user : 
            return HttpResponse("Já existe um usuário com esse nome")

        else:
            user = User.objects.create_user()
        return HttpResponse('oi')


def login(request):
    return render (request, 'login.html')"""