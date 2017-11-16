# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class LibroForm(forms.ModelForm):
	class Meta:
		model = Libro
		fields = '__all__'
		widgets = {
			'referencia': TextInput(attrs = {'class': 'form-control', 'maxlength': '10', 'required': True}),
			'nombre_libro': TextInput(attrs = {'class': 'form-control', 'maxlength': '200', 'required': True}),
			'nombre_autor': TextInput(attrs = {'class': 'form-control', 'maxlength': '45', 'required': True}),
			'descripcion': TextInput(attrs = {'class': 'form-control', 'maxlength': '200', 'required': True}),
			'isbn': TextInput(attrs = {'class': 'form-control', 'maxlength': '20', 'required': True}),
		}