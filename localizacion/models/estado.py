# -*- coding: utf-8 *-*
from django.db import models


class Estado (models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        app_label = 'localizacion'
