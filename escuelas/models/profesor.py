# -*- coding: utf-8 *-*
from django.db import models


class Profesor (models.Model):
    registro_profesor = models.CharField(max_length=20, unique=True)
    ape_paterno = models.CharField(max_length=25)
    ape_materno = models.CharField(max_length=25)
    nom_profesor = models.CharField(max_length=80)
    email = models.CharField(max_length=45)
    tel_celular = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    cod_postal = models.CharField(max_length=5, blank=True)

    def __unicode__(self):
        return self.nom_profesor

    class Meta:
        app_label = 'escuelas'
