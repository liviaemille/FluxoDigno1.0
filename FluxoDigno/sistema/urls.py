from django.urls import path
from . import views
#from .views import DoacaoCreateView

urlpatterns = [
    path('historico/', views.ver_doacoes, name='historico'),
    path('novadoacao/', views.nova_doacao, name='nova_doacao'),
    path('editardoacao/<int:id>/', views.editar_doacao, name='editar_doacao'),
    path('pontoscoleta/', views.ver_pontoscoleta, name='lista_pontoscoleta'),
#    path('editarponto/<int:id>/', views.editar_pontocoleta, name='editar_ponto'),
    path('sobrenos/', views.sobre_nos, name='sobrenos'),
    path('minhasdoacoes/', views.minhas_doacoes, name='minhasdoacoes'),
    path('novoposto/', views.novo_pontocoleta, name='novo_posto')
]