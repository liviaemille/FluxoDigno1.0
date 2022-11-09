from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from .forms import LoginForm
from .forms import NovoUsuarioForm
# Create your views here.


def registro(request):
    if request.user.is_authenticated:
        return redirect ('/home')
    else:
        if request.method == "POST":
            form_registro = NovoUsuarioForm(request.POST)
            if form_registro.is_valid():
                user = form_registro.save()
                login(request, user)
                messages.success(request, "Registration successful." )
                return redirect("/home")
            messages.error(request, "Não foi possível realizar cadastro. Tente novamente com iformações válidas!")
        form_registro = NovoUsuarioForm()
        return render(request, "../templates/sistema/registro.html", {"form_registro": form_registro})


def entrar(request): 
    if request.user.is_authenticated:
        return redirect ('/home')
    else :
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                usuario = authenticate(username=cd['username'], password=cd['password'])
                if usuario :
                    login(request, usuario)
                    return redirect('/home')
                else :
                    messages.info(request, 'Usuário ou senha inválidos')
                    return redirect('/login')
            else:
                return redirect('/login')
        else :
            form = LoginForm()
            return render(request, '../templates/sistema/login.html', {'form': form})
        

def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/home/')
        else:
            messages.warning(
                request, 'There was an error changing your password!')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, '../templates/sistema/alterarsenha.html', {'form': form})


def sair(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/login")
    


def index(request):
    if request.user.is_authenticated:
        return render(request, '../templates/sistema/index.html')
    else:
        return redirect('/login')