# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('prerequisites', models.TextField(blank=True)),
                ('requirements', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('time', models.DurationField(default=datetime.timedelta(0), blank=True)),
                ('requirements', models.TextField(blank=True)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LessonType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveSmallIntegerField(unique=True)),
                ('course', models.ForeignKey(to='syllabus.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('url', models.TextField()),
                ('lesson', models.ForeignKey(to='syllabus.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='unit',
            name='type',
            field=models.ForeignKey(to='syllabus.UnitType'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(to='syllabus.Module'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(to='syllabus.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='type',
            field=models.ForeignKey(to='syllabus.LessonType'),
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set([('module', 'order')]),
        ),
    ]
