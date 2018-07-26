from django.shortcuts import render
from .models import Evento, DiretoriaAtual


def index(request):
    return render(request, 'sucesuview/index.html', {})

def quem_somos(request):
    return render(request, 'sucesuview/quem_somos.html', {})

def diretoria_atual(request):
    diretores = DiretoriaAtual.objects.all()

    return render(request, 'sucesuview/diretoria_atual.html', {'diretores': diretores})

def sucesu_nacional(request):
    return render(request, 'sucesuview/sucesu_nacional.html', {})

def gestoes_anteriotes(request):
    return render(request, 'sucesuview/gestoes_anteriotes.html', {})

def estatuto_regimento(request):
    return render(request, 'sucesuview/estatuto_regimento.html', {})

def associados(request):
    return render(request, 'sucesuview/associados.html', {})

def parceiros(request):
    return render(request, 'sucesuview/parceiros.html', {})

def eventos(request):
    lista_eventos = Evento.objects.all().order_by('data')
    return render(request, 'sucesuview/eventos.html', {'eventos': lista_eventos})

def contato(request):
    return render(request, 'sucesuview/contato.html', {})

def cadastro(request):
    return render(request, 'sucesuview/cadastro.html', {})

def associe_se(request):
    return render(request, 'sucesuview/associe-se.html', {})

def agenda(request):
    return render(request, 'sucesuview/agenda.html', {})

def contato(request):
    return render(request, 'sucesuview/contato.html', {})

def evento(request):
    return render(request, 'sucesuview/detalhe_evento.html', {})

def inscreva_se_evento(request):
    return render(request, 'sucesuview/inscreva-se_evento.html', {})