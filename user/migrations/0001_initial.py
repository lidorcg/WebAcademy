# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0023_course_instructors'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, to='syllabus.Course')),
                ('lesson', models.ForeignKey(blank=True, to='syllabus.Lesson')),
                ('module', models.ForeignKey(blank=True, to='syllabus.Module')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
