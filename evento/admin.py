from django.contrib import admin
from .models import Evento, Palestrante, Pergunta


class PalestrantesEmLinha(admin.StackedInline):
    model = Palestrante

class PerguntaEmLinha(admin.StackedInline):
    model = Pergunta
    # readonly_fields = ['nome', 'palestrante','evento','pegunta']


class EventoAdmin(admin.ModelAdmin):
    inlines = [PalestrantesEmLinha, PerguntaEmLinha]


admin.site.register(Evento, EventoAdmin)