# -*- coding: utf-8 *-*
from django.db import models
from localizacion.models import Municipio


class Escuela (models.Model):
    registro_sep = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=80)
    id_municipio = models.ForeignKey(Municipio)
    direccion = models.CharField(max_length=100, blank=True)
    cod_postal = models.CharField(max_length=5, blank=True)
    tipo_escuela = models.CharField(max_length=1, blank=True)
    nivel_educativo = models.CharField(max_length=1, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        app_label = 'escuelas'
