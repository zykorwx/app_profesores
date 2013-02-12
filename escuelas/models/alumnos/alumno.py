# -*- coding: utf-8 *-*
from django.db import models
from tutor import Tutor


class Alumno (models.Model):
    ape_paterno = models.CharField(max_length=25)
    ape_materno = models.CharField(max_length=25)
    nom_alumno = models.CharField(max_length=80)
    id_tutor_1 = models.ForeignKey(Tutor)
    id_tutor_2 = models.ForeignKey(Tutor)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1)
    email = models.CharField(max_length=45)
    fecha_alta = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nom_profesor

    class Meta:
        app_label = 'escuelas'
