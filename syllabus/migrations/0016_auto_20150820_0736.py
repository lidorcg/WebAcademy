# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0015_auto_20150820_0718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='link',
            new_name='url',
        ),
    ]
