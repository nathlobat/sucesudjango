from django.db import models
from django.utils import timezone
#from sucesuview.models import Post


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    sobre = models.TextField()
    local = models.CharField(max_length=200)
    data = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False, default=None)
    imagem = models.ImageField(upload_to='images/eventos/%Y-%m/%d')


class DiretoriaAtual(models.Model):
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='images/diretoria/%Y-%m/%d')

class Assossiado(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='images/associados/%Y-%m/%d')


class Parceiro(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='images/parceiros/%Y-%m/%d')