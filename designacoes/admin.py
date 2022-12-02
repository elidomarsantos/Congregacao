from django.contrib import admin

from contatos.models import Contatos
from contas.models import Gerais, Contas

from designacoes.models import DesigQuarta, DesigSabado

admin.site.register(DesigQuarta)
admin.site.register(DesigSabado)
admin.site.register(Contatos)
admin.site.register(Gerais)
admin.site.register(Contas)
