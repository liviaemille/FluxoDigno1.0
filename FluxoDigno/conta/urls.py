from django.urls import re_path, path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.index, name='tela_inicio'),
    path('cadastro/', views.registro, name='cadastro'),
    path('logout/', views.sair, name='logout'),
    path('alterarsenha/', views.alterar_senha, name='alterarsenha'),
    path('login/', views.entrar, name='login')
    #path('editardoacao/<int:id>/', views.editar_doacao, name='editar_doacao'),
    #path('pontoscoleta/', views.ver_pontoscoleta, name='lista_pontoscoleta'),
    #path('sobrenos/', views.sobre_nos, name='sobrenos'),
]