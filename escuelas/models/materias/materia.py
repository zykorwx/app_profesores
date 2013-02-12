# -*- coding: utf-8 *-*
from django.db import models


class Materia (models.Model):
    registro_sep = models.CharField(max_length=20, unique=True)
    nivel_educativo = models.CharField(max_length=1)
    a_escolar = models.IntegerField(max_length=4)
    tipo_escuela = models.CharField(max_length=1)
    nombre_materia = models.CharField(max_length=45)

    def __unicode__(self):
        return self.nombre_materia

    class Meta:
        app_label = 'escuelas'
