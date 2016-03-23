# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0025_auto_20151022_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='level',
        ),
    ]
