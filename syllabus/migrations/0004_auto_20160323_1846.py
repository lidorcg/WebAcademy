# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0003_course_instructors'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleLevel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='unit',
            name='url',
            field=models.TextField(blank=True),
        ),
    ]
