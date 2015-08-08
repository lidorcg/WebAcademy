# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('syllabus', '0003_auto_20150806_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='concept',
            name='covered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='content',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='content',
            name='requirements',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='requirements',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='order',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='order',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]
