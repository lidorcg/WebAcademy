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

    def get_lectures_time(self):
        return sum_timedelta(m.get_lectures_time() for m in self.get_modules())

    def get_assignments_time(self):
        return sum_timedelta(m.get_assignments_time() for m in self.get_modules())

    def get_quiz_time(self):
        return sum_timedelta(m.get_quiz_time() for m in self.get_modules())

    def get_test_time(self):
        return sum_timedelta(m.get_test_time() for m in self.get_modules())

    def get_time(self):
        return sum_timedelta(m.get_time() for m in self.module_set.all())


class Module(models.Model):
    course = models.ForeignKey('Course')
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.title

    def get_contents(self):
        return self.content_set.order_by('order')

    def get_concepts(self):
        # ToDo find python/django way to write this function
        lst = []
        for c in self.get_contents():
            lst += c.concepts.all()
        return lst

    def get_progress(self):
        if self.content_set.count() == 0:
            return 1
        return self.content_set.filter(done=True).count() / self.content_set.count()

    def get_lectures_time(self):
        return sum_timedelta(c.time for c in self.content_set.filter(type__name='Lecture'))

    def get_assignments_time(self):
        return sum_timedelta(c.time for c in self.content_set.filter(type__name='Assignment'))

    def get_quiz_time(self):
        return sum_timedelta(c.time for c in self.content_set.filter(type__name='Quiz'))

    def get_test_time(self):
        return sum_timedelta(c.time for c in self.content_set.filter(type__name='Test'))

    def get_time(self):
        return sum_timedelta(c.time for c in self.content_set.all())


class Content(models.Model):
    module = models.ForeignKey('Module')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type = models.ForeignKey('Type')
    time = models.DurationField()
    concepts = models.ManyToManyField('Concept', blank=True)
    requirements = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField()
    done = models.BooleanField(default=False)

    class Meta:
        unique_together = (("module", "order"),)

    def __str__(self):
        return self.title


class Concept(models.Model):
    name = models.CharField(max_length=100)
    covered = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ToDo add tooltip messages
# ToDo add files upload and links to content
