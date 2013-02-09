# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Estado'
        db.create_table('localizacion_estado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=80)),
        ))
        db.send_create_signal('localizacion', ['Estado'])

        # Adding model 'Municipio'
        db.create_table('localizacion_municipio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=80)),
            ('id_estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['localizacion.Estado'])),
        ))
        db.send_create_signal('localizacion', ['Municipio'])

        # Adding model 'Junta_auxiliar'
        db.create_table('localizacion_junta_auxiliar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=80)),
            ('id_municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['localizacion.Municipio'])),
        ))
        db.send_create_signal('localizacion', ['Junta_auxiliar'])


    def backwards(self, orm):
        # Deleting model 'Estado'
        db.delete_table('localizacion_estado')

        # Deleting model 'Municipio'
        db.delete_table('localizacion_municipio')

        # Deleting model 'Junta_auxiliar'
        db.delete_table('localizacion_junta_auxiliar')


    models = {
        'localizacion.estado': {
            'Meta': {'object_name': 'Estado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        'localizacion.junta_auxiliar': {
            'Meta': {'object_name': 'Junta_auxiliar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localizacion.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        'localizacion.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localizacion.Estado']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        }
    }

    complete_apps = ['localizacion']