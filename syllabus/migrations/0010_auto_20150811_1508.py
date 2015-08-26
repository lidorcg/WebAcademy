# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0009_auto_20150811_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='time',
            field=models.DurationField(default=datetime.timedelta(0), blank=True),
        ),
    ]