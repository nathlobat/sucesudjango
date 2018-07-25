from django.db import models
from django.utils import timezone
#from sucesuview.models import Post


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    sobre = models.TextField()
    local = models.CharField(max_length=200)
    data = models.DateTimeField()
    imagem = models.ImageField(upload_to='images/%Y/%m/%d')