from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from models import *

class IndexView(generic.View):

	def get(self, request, *args, **kwargs):
		return render(request,'page/index.html')

class ExpedientesView(generic.View):

	def get(self, request, *args, **kwargs):
		lista		= Expediente.objects.all()
		paginator	= Paginator(lista, 15)
		page 		= request.GET.get('page')

		try:
			expedientes = paginator.page(page)
		except PageNotAnInteger:
			expedientes = paginator.page(1)
		except EmptyPage:
			expedientes = paginator.page(paginator.num_pages)

		return render(request,'page/expediente/expediente.html',{'expedientes':expedientes})

class ExpedienteCreate(generic.CreateView):
	model 			= Expediente
	template_name	= 'page/expediente/expediente_form.html'
	fields 			= [	'nro_instruccion','nro_expediente','anio','juzgado','agraviado',
						'inculpado','materia','nro_fojas','nro_legajo']
	success_url 	= reverse_lazy('page:expediente')

class ExpedienteUpdate(generic.UpdateView):
	model 			= Expediente
	template_name	= 'page/expediente/expediente_form.html'
	fields 			= [	'nro_instruccion','nro_expediente','anio','juzgado','agraviado',
						'inculpado','materia','nro_fojas','nro_legajo']
	success_url 	= reverse_lazy('page:expediente')

class ExpedienteDelete(generic.DeleteView):
	model 			= Expediente
	template_name	= 'page/expediente/expediente_delete.html'
	success_url		= reverse_lazy('page:expediente_delete')

class ExpedienteBuscar(generic.View):

	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscalo']
		opcion = request.POST['opcion']

		if(opcion == '1'):
			expedientes = Expediente.objects.filter(nro_instruccion__contains=buscar)
			contexto = {'expedientes':expedientes,'expediente':True}
			return render(request,'page/expediente/expediente_search.html',contexto)
		if(opcion == '2'):
			expedientes = Expediente.objects.filter(nro_expediente__contains=buscar)
			contexto = {'expedientes':expedientes,'expediente':True}
			return render(request,'page/expediente/expediente_search.html',contexto)
		if(opcion == '3'):
			expedientes = Expediente.objects.filter(agraviado__contains=buscar)
			contexto = {'expedientes':expedientes,'expediente':True}
			return render(request,'page/expediente/expediente_search.html',contexto)
		if(opcion == '4'):
			expedientes = Expediente.objects.filter(inculpado__contains=buscar)
			contexto = {'expedientes':expedientes,'expediente':True}
			return render(request,'page/expediente/expediente_search.html',contexto)
		if(opcion == '5'):
			expedientes = Expediente.objects.filter(materia__contains=buscar)
			contexto = {'expedientes':expedientes,'expediente':True}
			return render(request,'page/expediente/expediente_search.html',contexto)
		if(opcion == '6'):
			expedientes = Expediente.objects.filter(nro_legajo__contains=buscar)
			contexto = {'expedientes':expedientes,'expediente':True}
			return render(request,'page/expediente/expediente_search.html',contexto)
		else:
			return render(request,'page/expediente/expediente_search.html')

class ExpedienteSearch(generic.View):

	def get(self, request, *args, **kwargs):
		return render(request,'page/expediente/expediente_search_get.html')