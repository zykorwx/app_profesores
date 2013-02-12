# -*- coding: utf-8 *-*
from django.db import models


class Tutor (models.Model):
    ape_paterno = models.CharField(max_length=25)
    ape_materno = models.CharField(max_length=25)
    nom_tutor = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    fecha_alta = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=45)
    sexo = models.CharField(max_lenght=1)

    def __unicode__(self):
        return self.nom_tutor

    class Meta:
        app_label = 'escuelas'
