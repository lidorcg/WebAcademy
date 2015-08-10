# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0006_auto_20150810_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='concepts',
            field=models.ManyToManyField(blank=True, to='syllabus.Concept'),
        ),
    ]
