# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wizard', '0004_auto_20151228_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='shallowcourse',
            name='user',
        ),
        migrations.DeleteModel(
            name='ShallowCourse',
        ),
        migrations.AddField(
            model_name='group',
            name='course',
            field=models.ForeignKey(to='wizard.Idea', default=None),
            preserve_default=False,
        ),
    ]
