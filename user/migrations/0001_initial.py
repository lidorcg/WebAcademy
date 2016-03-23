# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('syllabus', '0003_course_instructors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, to='syllabus.Course', null=True)),
                ('lesson', models.ForeignKey(blank=True, to='syllabus.Lesson', null=True)),
                ('module', models.ForeignKey(blank=True, to='syllabus.Module', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
