from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from .helper import *


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prerequisites = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    instructors = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('syllabus:course-detail', args=[str(self.id)])

    def get_modules(self):
        return self.module_set.order_by('order')

    def get_modules_count(self):
        return self.get_modules().count()

    def get_messages(self):
        return self.message_set.order_by('date')

    def get_progress(self):
        if self.module_set.count() == 0:
            return 1
        return sum(m.get_progress() for m in self.module_set.all()) / self.module_set.count()

    def get_learn_time(self):
        return sum_timedelta(m.get_learn_time() for m in self.get_modules())

    def get_practice_time(self):
        return sum_timedelta(m.get_practice_time() for m in self.get_modules())

    def get_test_time(self):
        return sum_timedelta(m.get_test_time() for m in self.get_modules())

    def get_time(self):
        return sum_timedelta(m.get_time() for m in self.module_set.all())


class Module(models.Model):
    course = models.ForeignKey('Course')
    order = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    level = models.ForeignKey('ModuleLevel')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('syllabus:course-detail', args=[str(self.course_id)])

    def get_lessons(self):
        return self.lesson_set.order_by('order')

    def get_lessons_count(self):
        return self.get_lessons().count()

    def get_messages(self):
        return self.message_set.order_by('date')

    def get_tags(self):
        # ToDo find python/django way to write this function
        lst = []
        for c in self.get_lessons():
            lst += c.tags.all()
        return lst

    def get_progress(self):
        if self.lesson_set.count() == 0:
            return 1
        return self.get_lessons().filter(done=True).count() / self.get_lessons_count()

    def get_time_to(self, type_name):
        return sum_timedelta(c.time for c in self.get_lessons().filter(type__name=type_name))

    def get_learn_time(self):
        return self.get_time_to('Learn')

    def get_practice_time(self):
        return self.get_time_to('Practice')

    def get_test_time(self):
        return self.get_time_to('Test')

    def get_time(self):
        return sum_timedelta(c.time for c in self.lesson_set.all())


class Lesson(models.Model):
    module = models.ForeignKey('Module')
    order = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type = models.ForeignKey('LessonType')
    time = models.DurationField(blank=True, default=datetime.timedelta(0))
    requirements = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('syllabus:module-detail', args=[str(self.module_id)])

    def get_units(self):
        return self.unit_set.order_by('order')

    def get_units_count(self):
        return self.get_units().count()

    def get_messages(self):
        return self.message_set.order_by('date')

    def get_time(self):
        return self.time


class Unit(models.Model):
    lesson = models.ForeignKey('Lesson')
    order = models.PositiveSmallIntegerField()
    type = models.ForeignKey('UnitType')
    name = models.CharField(max_length=100)
    url = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('syllabus:lesson-detail', args=[str(self.lesson_id)])


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ModuleLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LessonType(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class UnitType(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

# ToDo add knowledge level for lesson
# ToDo add practice and tests templates for the different knowledge level
