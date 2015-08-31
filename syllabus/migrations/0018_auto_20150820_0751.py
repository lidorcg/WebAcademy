# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('syllabus', '0017_auto_20150820_0743'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='LessonType',
        ),
    ]
