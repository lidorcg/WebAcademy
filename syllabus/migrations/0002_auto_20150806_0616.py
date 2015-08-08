# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('syllabus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='ContentConcept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concept', models.ForeignKey(to='syllabus.Concept')),
                ('content', models.ForeignKey(to='syllabus.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='concepts',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='module',
        ),
        migrations.RemoveField(
            model_name='assignmentconcept',
            name='assignment',
        ),
        migrations.RemoveField(
            model_name='assignmentconcept',
            name='concept',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='concepts',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='module',
        ),
        migrations.RemoveField(
            model_name='lectureconcept',
            name='concept',
        ),
        migrations.RemoveField(
            model_name='lectureconcept',
            name='lecture',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='concepts',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='module',
        ),
        migrations.RemoveField(
            model_name='quizconcept',
            name='concept',
        ),
        migrations.RemoveField(
            model_name='quizconcept',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='AssignmentConcept',
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
        migrations.DeleteModel(
            name='LectureConcept',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='QuizConcept',
        ),
        migrations.AddField(
            model_name='content',
            name='concepts',
            field=models.ManyToManyField(to='syllabus.Concept', through='syllabus.ContentConcept'),
        ),
        migrations.AddField(
            model_name='content',
            name='module',
            field=models.ForeignKey(to='syllabus.Module'),
        ),
        migrations.AddField(
            model_name='content',
            name='type',
            field=models.ForeignKey(to='syllabus.Type'),
        ),
    ]
