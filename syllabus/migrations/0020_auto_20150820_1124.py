# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('syllabus', '0019_auto_20150820_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessontype',
            name='tooltip',
        ),
        migrations.RemoveField(
            model_name='unittype',
            name='tooltip',
        ),
    ]
