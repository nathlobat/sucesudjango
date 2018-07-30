from django.contrib import admin
from .models import Evento, DiretoriaAtual, Assossiados, Parceiros


admin.site.register(Evento)
admin.site.register(DiretoriaAtual)
admin.site.register(Assossiados)
admin.site.register(Parceiros)
