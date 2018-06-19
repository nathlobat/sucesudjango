from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quem_somos/', views.quem_somos, name='quem_somos'),
    path('diretoria_atual/', views.diretoria_atual, name='diretoria_atual'),
    path('sucesu_nacional/', views.sucesu_nacional, name='sucesu_nacional'),
    path('gestoes_anteriores/', views.gestoes_anteriotes, name='gestoes_anteriotes'),
    path('estatuto_regimento/', views.estatuto_regimento, name='estatuto_regimento'),
    path('associados/', views.associados, name='associados'),
    path('parceiros/', views.parceiros, name='parceiros'),
    path('eventos/', views.eventos, name='eventos'),
    path('contato/', views.contato, name='contato'),
]
