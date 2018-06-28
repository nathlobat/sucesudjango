from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quem_somos/', views.quem_somos, name='quem_somos'),
    path('diretoria_atual/', views.diretoria_atual, name='diretoria_atual'),
    path('sucesu_nacional/', views.sucesu_nacional, name='sucesu_nacional'),
    path('gestoes_anteriores/', views.gestoes_anteriotes, name='gestoes_anteriotes'),
    path('estatuto_regimento/', views.estatuto_regimento, name='estatuto_regimento'),
    path('agenda/', views.agenda, name='agenda),
	path('associados/', views.associados, name='associados'),
	path('associe-se/', views.associe-se, name='associe-se'),
	path('base/', views.base, name='base'),
	path('cadastro/', views.cadastro, name='cadastro'),
	path('contact/', views.contact, name='contact'),
    path('detalhe_evento/', views.detalhe_evento, name='detalhe_evento'),
	path('detalhe_evento2/', views.detalhe_evento2, name='detalhe_evento2'),
	path('eventos/', views.eventos, name='eventos'),
	path('inscreva-se_evento/', views.inscreva-se_evento, name='inscreva-se_evento'),
	path('parceiros/', views.parceiros, name='parceiros'),
	path('post_list/', views.post_list, name='post_list'),
	
]
