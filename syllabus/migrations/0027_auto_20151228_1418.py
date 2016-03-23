# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0026_remove_module_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='url',
            field=models.TextField(blank=True),
        ),
    ]
