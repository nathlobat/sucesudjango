from django.contrib import admin
from .models import Evento, DiretoriaAtual, Associado, Parceiro


admin.site.register(Evento)
admin.site.register(DiretoriaAtual)
admin.site.register(Associado)
admin.site.register(Parceiro)
