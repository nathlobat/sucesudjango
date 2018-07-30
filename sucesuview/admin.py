from django.contrib import admin
from .models import Evento, DiretoriaAtual, Assossiado, Parceiro


admin.site.register(Evento)
admin.site.register(DiretoriaAtual)
admin.site.register(Assossiado)
admin.site.register(Parceiro)
