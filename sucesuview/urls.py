from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quem_somos/', views.quem_somos, name='quem_somos'),
    path('diretoria_atual/', views.diretoria_atual, name='diretoria_atual'),
    path('sucesu_nacional/', views.sucesu_nacional, name='sucesu_nacional'),
    path('gestoes_anteriores/', views.gestoes_anteriotes, name='gestoes_anteriotes'),
    path('estatuto_regimento/', views.estatuto_regimento, name='estatuto_regimento'),
    path('agenda/', views.agenda, name='agenda'),
	path('associados/', views.associados, name='associados'),
	path('associe-se/', views.associe_se, name='associe_se'),
	path('cadastro/', views.cadastro, name='cadastro'),
	path('contato/', views.contato, name='contato'),
    path('evento/', views.detalhe_evento, name='evento'),
	path('eventos/', views.eventos, name='eventos'),
	path('inscreva-se/', views.inscreva_se_evento, name='inscreva-se_evento'),
	path('parceiros/', views.parceiros, name='parceiros'),
	
]
