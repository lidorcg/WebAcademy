# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0010_auto_20150811_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
