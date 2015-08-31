# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('syllabus', '0007_auto_20150810_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='time',
            field=models.DurationField(blank=True),
        ),
    ]
