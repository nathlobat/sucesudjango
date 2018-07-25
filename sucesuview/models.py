from django.db import models
from django.utils import timezone
#from sucesuview.models import Post


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    sobre = models.TextField()
    local = models.CharField(max_length=200)
    data = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False, default=None)
    imagem = models.ImageField(upload_to='images/%Y/%m/%d')