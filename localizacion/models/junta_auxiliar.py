from django.db import models
from municipio import Municipio


class Junta_auxiliar (models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    id_municipio = models.ForeignKey(Municipio)

    def __unicode__(self):
        return self.nombre

    class Meta:
        app_label = 'localizacion'
