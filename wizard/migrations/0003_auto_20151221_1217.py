# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0002_auto_20151116_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Tag',
            new_name='Group',
        ),
        migrations.AddField(
            model_name='concept',
            name='group',
            field=models.ForeignKey(default=None, to='wizard.Group', null=True, blank=True),
        ),
    ]
