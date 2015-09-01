# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='order',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set([]),
        ),
    ]
