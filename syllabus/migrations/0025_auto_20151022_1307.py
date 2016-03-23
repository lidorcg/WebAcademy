# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0024_auto_20151022_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='level',
        ),
        migrations.DeleteModel(
            name='LessonLevel',
        ),
        migrations.AddField(
            model_name='module',
            name='level',
            field=models.ForeignKey(to='syllabus.ModuleLevel', default=1),
            preserve_default=False,
        ),
    ]
