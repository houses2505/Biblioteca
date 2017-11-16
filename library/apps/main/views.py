# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import *
from django.db.models import Q
from .models import *
from .forms import *

template_dir = 'libros/'


class HomeView(TemplateView):
	template_name = template_dir+'home.html'

class LibroView(ListView):
	model = Libro
	paginate_by = 20
	template_name = template_dir+'lista.html'

	def get_queryset(self):
		queryset = super(LibroView, self).get_queryset().order_by('nombre_libro')
		if self.request.GET.get('word') is not None:
			find_by = self.request.GET.get('word')
			queryset = queryset.filter(Q(referencia__icontains = find_by) | Q(nombre_libro__icontains = find_by) | Q(nombre_autor__icontains = find_by) | Q(descripcion__icontains = find_by) | Q(isbn__icontains = find_by))
		return queryset

class BookDetailView(DetailView):
	model = Libro
	template_name = template_dir+'detalle_libro.html'

class LibroCreateView(CreateView):
	template_name = template_dir+'form_libro.html'
	success_message = 'Libro agregado correctamente'
	form_class = LibroForm

	def get_context_data(self, **kwargs):
		context = super(LibroCreateView, self).get_context_data(**kwargs)
		context['url'] = '/crear/'
		return context

	def get_success_url(self):
		return reverse('lista_libro')

class LibroUpdateView(UpdateView):
	model = Libro
	template_name = template_dir+'form_libro.html'
	success_message = 'Libro actualizado correctamente'
	form_class = LibroForm

	def get_context_data(self, **kwargs):
		context = super(LibroUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar proyecto'
		context['url'] = '/actualizar/'+self.kwargs['pk']
		return context

	def get_success_url(self):
		return reverse('LibroUpdateView',args=(self.object.id,))

class LibroDeleteView(DeleteView):
	model = Libro
	template_name = template_dir+'delete_general.html'

	def get_context_data(self, **kwargs):
		context = super(LibroDeleteView, self).get_context_data(**kwargs)
		context['url'] = '/proyecto/'+self.kwargs['pk']+'/eliminar/'
		return context

	def get_success_url(self):
		return reverse('home')