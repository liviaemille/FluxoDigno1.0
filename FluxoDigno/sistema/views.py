from django.shortcuts import render, redirect
from .forms import DoacoesForm
from .models import Doacoes, pontosColeta
from django.http import HttpResponse
#from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django import forms

def sobre_nos (request):
    return render(request, "../templates/sistema/sobrenos.html")


def nova_doacao(request):
    form = DoacoesForm(request.POST or None)
    
    doador = request.user
    if form.is_valid():
        produto = form.cleaned_data['produto']
        data = form.cleaned_data['data']
        pontocoleta = form.cleaned_data['pontocoleta']
        doacao = Doacoes.objects.create(produto=produto, data=data, doador=doador, pontocoleta=pontocoleta)
        doacao.save()
        return redirect('/historico')
    return render(request, '../templates/sistema/doacoes_form.html', {'form': form})

def ver_doacoes(request):
    doacoes = Doacoes.objects.all()
    return render (request, '../templates/sistema/historico.html', {'doacoes': doacoes})

def minhas_doacoes (request):
    iduser = request.user.id
    doacoes = Doacoes.objects.filter(doador=iduser)
    return render (request, '../templates/sistema/minhasdoacoes.html', {'doacoes': doacoes})

def editar_doacao(request, id):
    doacao = Doacoes.objects.get(id=id)
    form = DoacoesForm(request.POST or None, instance=doacao)

    if form.is_valid():
        form.save()
        return redirect('/minhasdoacoes')

    return render(request, '../templates/sistema/editardoacao.html', {'form': form, 'doacao': doacao})

def deletar_doacao(request, id):

    doacao = Doacoes.objects.get(id=id)

    if request.method == 'POST':
        doacao.delete()
        return redirect('lista_produtos')

    return render(request, '../templates/sistema/', {'doacao': doacao })

def ver_pontoscoleta(request):
    pontos = pontosColeta.objects.all()
    return render (request, '../templates/sistema/postos.html', {"pontos": pontos})
