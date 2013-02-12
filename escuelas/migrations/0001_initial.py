# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Escuela'
        db.create_table('escuelas_escuela', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registro_sep', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('id_municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['localizacion.Municipio'])),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cod_postal', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('tipo_escuela', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('nivel_educativo', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('escuelas', ['Escuela'])

        # Adding model 'Profesor'
        db.create_table('escuelas_profesor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registro_profesor', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('ape_paterno', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('ape_materno', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('nom_profesor', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('tel_celular', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cod_postal', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
        ))
        db.send_create_signal('escuelas', ['Profesor'])

        # Adding model 'Ciclo_escolar'
        db.create_table('escuelas_ciclo_escolar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_termino', self.gf('django.db.models.fields.DateField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('escuelas', ['Ciclo_escolar'])

        # Adding model 'Prof_alta'
        db.create_table('escuelas_prof_alta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_profesor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['escuelas.Profesor'])),
            ('id_registro_sep', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['escuelas.Escuela'])),
            ('estatus', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('fecha_alta', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('escuelas', ['Prof_alta'])

        # Adding model 'Materia'
        db.create_table('escuelas_materia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registro_sep', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('nivel_educativo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('a_escolar', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('tipo_escuela', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('nombre_materia', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal('escuelas', ['Materia'])

        # Adding model 'Tema_materia'
        db.create_table('escuelas_tema_materia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['escuelas.Materia'])),
            ('codigo_tema', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('nom_tema', self.gf('django.db.models.fields.CharField')(max_length=65)),
        ))
        db.send_create_signal('escuelas', ['Tema_materia'])


    def backwards(self, orm):
        # Deleting model 'Escuela'
        db.delete_table('escuelas_escuela')

        # Deleting model 'Profesor'
        db.delete_table('escuelas_profesor')

        # Deleting model 'Ciclo_escolar'
        db.delete_table('escuelas_ciclo_escolar')

        # Deleting model 'Prof_alta'
        db.delete_table('escuelas_prof_alta')

        # Deleting model 'Materia'
        db.delete_table('escuelas_materia')

        # Deleting model 'Tema_materia'
        db.delete_table('escuelas_tema_materia')


    models = {
        'escuelas.ciclo_escolar': {
            'Meta': {'object_name': 'Ciclo_escolar'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'fecha_termino': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'escuelas.escuela': {
            'Meta': {'object_name': 'Escuela'},
            'cod_postal': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localizacion.Municipio']"}),
            'nivel_educativo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'registro_sep': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'tipo_escuela': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'escuelas.materia': {
            'Meta': {'object_name': 'Materia'},
            'a_escolar': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_educativo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'nombre_materia': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'registro_sep': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'tipo_escuela': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'escuelas.prof_alta': {
            'Meta': {'object_name': 'Prof_alta'},
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['escuelas.Profesor']"}),
            'id_registro_sep': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['escuelas.Escuela']"})
        },
        'escuelas.profesor': {
            'Meta': {'object_name': 'Profesor'},
            'ape_materno': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'ape_paterno': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'cod_postal': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom_profesor': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'registro_profesor': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'tel_celular': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'escuelas.tema_materia': {
            'Meta': {'object_name': 'Tema_materia'},
            'codigo_tema': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_materia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['escuelas.Materia']"}),
            'nom_tema': ('django.db.models.fields.CharField', [], {'max_length': '65'})
        },
        'localizacion.estado': {
            'Meta': {'object_name': 'Estado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        'localizacion.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localizacion.Estado']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        }
    }

    complete_apps = ['escuelas']