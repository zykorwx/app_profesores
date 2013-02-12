# -*- coding: utf-8 *-*
from django.db import models
from materia import Materia


class Tema_materia (models.Model):
    id_materia = models.ForeignKey(Materia)
    codigo_tema = models.CharField(max_length=6)
    nom_tema = models.CharField(max_length=65)

    def __unicode__(self):
        return self.nom_tema

    class Meta:
        app_label = 'escuelas'
