# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentConcept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignment', models.ForeignKey(to='syllabus.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='LectureConcept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concept', models.ForeignKey(to='syllabus.Concept')),
                ('lecture', models.ForeignKey(to='syllabus.Lecture')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(to='syllabus.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='QuizConcept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concept', models.ForeignKey(to='syllabus.Concept')),
                ('quiz', models.ForeignKey(to='syllabus.Quiz')),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='concepts',
            field=models.ManyToManyField(to='syllabus.Concept', through='syllabus.QuizConcept'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='module',
            field=models.ForeignKey(to='syllabus.Module'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='concepts',
            field=models.ManyToManyField(to='syllabus.Concept', through='syllabus.LectureConcept'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='module',
            field=models.ForeignKey(to='syllabus.Module'),
        ),
        migrations.AddField(
            model_name='assignmentconcept',
            name='concept',
            field=models.ForeignKey(to='syllabus.Concept'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='concepts',
            field=models.ManyToManyField(to='syllabus.Concept', through='syllabus.AssignmentConcept'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='module',
            field=models.ForeignKey(to='syllabus.Module'),
        ),
    ]
