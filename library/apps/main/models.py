from __future__ import unicode_literals

from django.db import models

class Libro(models.Model):
	referencia = models.CharField(max_length = 10)
	nombre_libro = models.CharField(max_length = 200)
	nombre_autor = models.CharField(max_length = 45)
	descripcion = models.CharField(max_length = 200)
	isbn = models.CharField(max_length = 20)

	def __str__(self):
		return self.referencia

	def __unicode__(self):
		return self.referencia