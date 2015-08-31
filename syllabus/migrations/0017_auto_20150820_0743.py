# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('syllabus', '0016_auto_20150820_0736'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LinkType',
            new_name='UnitType',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='linkType',
            new_name='type',
        ),
    ]
