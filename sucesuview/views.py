from django.shortcuts import render

def index(request):
    return render(request, 'sucesuview/index.html', {})

def quem_somos(request):
    return render(request, 'sucesuview/quem_somos.html', {})

def diretoria_atual(request):
    return render(request, 'sucesuview/diretoria_atual.html', {})

def sucesu_nacional(request):
    return render(request, 'sucesuview/sucesu_nacional.html', {})

def gestoes_anteriotes(request):
    return render(request, 'sucesuview/gestoes_anteriotes.html', {})

def estatuto_regimento(request):
    return render(request, 'sucesuview/estatuto_regimento.html', {})
