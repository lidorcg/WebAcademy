# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('syllabus', '0011_auto_20150818_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='icon',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
