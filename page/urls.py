from django.conf.urls import patterns, url
from page import views

urlpatterns = patterns('',

	# Vista
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'expedientes/$', views.ExpedientesView.as_view(), name='expediente'),
	url(r'expediente/create/$', views.ExpedienteCreate.as_view(), name='expediente_create'),
	url(r'expediente/update/(?P<pk>\d+)/$', views.ExpedienteUpdate.as_view(), name='expediente_update'),
	url(r'expediente/delete/(?P<pk>\d+)/$', views.ExpedienteDelete.as_view(), name='expediente_delete'),
	url(r'expediente/buscar/$', views.ExpedienteBuscar.as_view(), name='expediente_buscar'),
	url(r'expediente/search/$', views.ExpedienteSearch.as_view(), name='expediente_search'),
)