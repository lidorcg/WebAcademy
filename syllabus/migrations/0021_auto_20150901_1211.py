# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0020_auto_20150820_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='order',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
