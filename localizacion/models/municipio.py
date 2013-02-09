# -*- coding: utf-8 *-*
from django.db import models
from estado import Estado


class Municipio (models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    id_estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return self.nombre

    class Meta:
        app_label = 'localizacion'
