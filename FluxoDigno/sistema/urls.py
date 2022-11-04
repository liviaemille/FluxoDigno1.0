from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_inicio, name='tela_inicio'),
    path('doacoes/', views.ver_doacoes, name='lista_doacoes'),
    path('novadoacao/', views.nova_doacao, name='nova_doacao'),
    path('editardoacao/<int:id>/', views.editar_doacao, name='editar_doacao'),
    path('pontoscoleta/', views.ver_pontoscoleta, name='lista_pontoscoleta'),
]