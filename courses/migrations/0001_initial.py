# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table(u'courses_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_description', self.gf('django.db.models.fields.TextField')(max_length=160)),
        ))
        db.send_create_signal(u'courses', ['Course'])

        # Adding M2M table for field parents on 'Course'
        m2m_table_name = db.shorten_name(u'courses_course_parents')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_course', models.ForeignKey(orm[u'courses.course'], null=False)),
            ('to_course', models.ForeignKey(orm[u'courses.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_course_id', 'to_course_id'])


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table(u'courses_course')

        # Removing M2M table for field parents on 'Course'
        db.delete_table(db.shorten_name(u'courses_course_parents'))


    models = {
        u'courses.course': {
            'Meta': {'ordering': "['title']", 'object_name': 'Course'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'parents_rel_+'", 'to': u"orm['courses.Course']"}),
            'short_description': ('django.db.models.fields.TextField', [], {'max_length': '160'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['courses']