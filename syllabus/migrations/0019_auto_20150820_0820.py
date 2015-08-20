# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0018_auto_20150820_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessontype',
            name='tooltip',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='unittype',
            name='tooltip',
            field=models.TextField(blank=True),
        ),
    ]
