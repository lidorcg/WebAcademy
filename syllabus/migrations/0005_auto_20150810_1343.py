# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0004_auto_20150808_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentconcept',
            name='concept',
        ),
        migrations.RemoveField(
            model_name='contentconcept',
            name='content',
        ),
        migrations.AddField(
            model_name='content',
            name='concepts2',
            field=models.ManyToManyField(to='syllabus.Concept'),
        ),
        migrations.AlterField(
            model_name='content',
            name='order',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='content',
            unique_together=set([('module', 'order')]),
        ),
        migrations.RemoveField(
            model_name='content',
            name='concepts',
        ),
        migrations.DeleteModel(
            name='ContentConcept',
        ),
    ]
