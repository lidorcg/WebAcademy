# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0023_course_instructors'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonLevel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='level',
            field=models.ForeignKey(default=1, to='syllabus.LessonLevel'),
            preserve_default=False,
        ),
    ]
