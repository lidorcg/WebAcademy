# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='course',
            field=models.ForeignKey(null=True, to='syllabus.Course', blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='lesson',
            field=models.ForeignKey(null=True, to='syllabus.Lesson', blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='module',
            field=models.ForeignKey(null=True, to='syllabus.Module', blank=True),
        ),
    ]
