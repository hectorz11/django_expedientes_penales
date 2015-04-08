from django.contrib import admin
from .models import *

class ExpedienteAdmin(admin.ModelAdmin):
	list_display = ('id','nro_instruccion','nro_expediente','juzgado','agraviado','inculpado','materia','nro_fojas','nro_legajo')
	search_fields = ['nro_instruccion','nro_expediente','agraviado','inculpado','materia','nro_legajo']
	list_filter = ('juzgado','materia')

admin.site.register(Expediente,ExpedienteAdmin)