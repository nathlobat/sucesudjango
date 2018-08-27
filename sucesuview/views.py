from django.shortcuts import render, get_object_or_404
from .models import Evento, DiretoriaAtual, Associado, Parceiro


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
    associados = Associado.objects.all()
    return render(request, 'sucesuview/associados.html', {'associados': associados})

def parceiros(request):
    parceiro = Parceiro.objects.all()
    return render(request, 'sucesuview/parceiros.html', {'parceiros': parceiro})


def eventos(request):
    lista_eventos = Evento.objects.all().order_by('data')
    return render(request, 'sucesuview/eventos.html', {'eventos': lista_eventos})

def detalhe_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'sucesuview/detalhe_evento.html', {'evento': evento})

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

def inscreva_se_evento(request):
    return render(request, 'sucesuview/inscreva-se_evento.html', {})
