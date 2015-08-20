# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0014_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='unit',
            name='lesson',
            field=models.ForeignKey(to='syllabus.Lesson', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='linkType',
            field=models.ForeignKey(to='syllabus.LinkType', default=''),
            preserve_default=False,
        ),
    ]
