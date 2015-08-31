# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('syllabus', '0005_auto_20150810_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='concepts2',
            new_name='concepts',
        ),
    ]
