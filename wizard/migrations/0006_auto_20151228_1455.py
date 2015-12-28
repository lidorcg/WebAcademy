# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0005_auto_20151228_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='course',
            field=models.ForeignKey(null=True, blank=True, default=None, to='wizard.Idea'),
        ),
    ]
