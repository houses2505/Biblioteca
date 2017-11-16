from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from .views import *

urlpatterns = patterns('library.apps.main.views',
	url(r'^$', HomeView.as_view(), name = 'home'),
	url(r'^libro/$', LibroView.as_view(), name = 'lista_libro'),
	url(r'^(?P<pk>\d+)/$', BookDetailView.as_view(), name = 'libro_detalle'),
	url(r'^actualizar/(?P<pk>\d+)/$', LibroUpdateView.as_view(), name='edit_libro'),
	url(r'^eliminar/$', LibroDeleteView.as_view(), name='delete_libro'),
	url(r'^crear/$', LibroCreateView.as_view(), name='crear_libro'),
)