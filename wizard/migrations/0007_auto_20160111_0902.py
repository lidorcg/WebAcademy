# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0006_auto_20151228_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='course',
        ),
        migrations.AddField(
            model_name='concept',
            name='idea',
            field=models.ForeignKey(to='wizard.Idea', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='idea',
            field=models.ForeignKey(to='wizard.Idea', default=None),
            preserve_default=False,
        ),
    ]
