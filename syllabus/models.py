from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_modules(self):
        return self.module_set.order_by('order')


class Module(models.Model):
    course = models.ForeignKey('Course')
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

    def get_content(self):
        return self.content_set.order_by('order')


class Content(models.Model):
    module = models.ForeignKey('Module')
    type = models.ForeignKey('Type')
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DurationField()  # ToDo duration in minutes
    concepts = models.ManyToManyField('Concept', through='ContentConcept')
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class Concept(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContentConcept(models.Model):
    content = models.ForeignKey('Content')
    concept = models.ForeignKey('Concept')
