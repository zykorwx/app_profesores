# -*- coding: utf-8 *-*
from django.db import models


class Ciclo_escolar (models.Model):
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        app_label = 'escuelas'
