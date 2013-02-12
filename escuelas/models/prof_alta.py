# -*- coding: utf-8 *-*
from django.db import models
from escuela import Escuela
from profesor import Profesor


class Prof_alta (models.Model):
    id_profesor = models.ForeignKey(Profesor)
    id_registro_sep = models.ForeignKey(Escuela)
    estatus = models.CharField(max_length=1)
    fecha_alta = models.DateTimeField()

    def __unicode__(self):
        return self.estatus

    class Meta:
        app_label = 'escuelas'
