# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0003_auto_20151221_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shallowcourse',
            name='prerequisites',
        ),
        migrations.RemoveField(
            model_name='shallowcourse',
            name='requirements',
        ),
    ]
