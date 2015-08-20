from django.db import models

from .helper import *


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prerequisites = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    # ToDo add creator relationship to User

    def __str__(self):
        return self.title

    def get_modules(self):
        return self.module_set.order_by('order')

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

    def get_modules_count(self):
        return self.get_modules().count()


class Module(models.Model):
    course = models.ForeignKey('Course')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.title

    def get_lessons(self):
        return self.lesson_set.order_by('order')

    def get_lessons_count(self):
        return self.get_lessons().count()

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
    type = models.ForeignKey('Type')
    time = models.DurationField(blank=True, default=datetime.timedelta(0))
    requirements = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    done = models.BooleanField(default=False)

    class Meta:
        unique_together = (("module", "order"),)

    def __str__(self):
        return self.title

    def get_time(self):
        return self.time


class Unit(models.Model):
    lesson = models.ForeignKey('Lesson')
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    link = models.TextField()
    linkType = models.ForeignKey('LinkType')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class LinkType(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

# ToDo add tooltip messages
# ToDo add files upload and links to Lesson
# ToDo add comments for documentation
