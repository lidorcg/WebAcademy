# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0008_auto_20150811_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='time',
            field=models.DurationField(blank=True, default=0),
        ),
    ]
