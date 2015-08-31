# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('syllabus', '0012_type_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('time', models.DurationField(blank=True, default=datetime.timedelta(0))),
                ('requirements', models.TextField(blank=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('done', models.BooleanField(default=False)),
                ('module', models.ForeignKey(to='syllabus.Module')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='content',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='content',
            name='concepts',
        ),
        migrations.RemoveField(
            model_name='content',
            name='module',
        ),
        migrations.RemoveField(
            model_name='content',
            name='type',
        ),
        migrations.DeleteModel(
            name='Concept',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.AddField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(to='syllabus.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='type',
            field=models.ForeignKey(to='syllabus.Type'),
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set([('module', 'order')]),
        ),
    ]
