from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey('Course')
    title = models.CharField(max_length=100)
    description = models.TextField()
    # ToDo create ordering field

    def __str__(self):
        return self.title


class Content(models.Model):
    module = models.ForeignKey('Module')
    type = models.ForeignKey('Type')
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DurationField()
    concepts = models.ManyToManyField('Concept', through='ContentConcept')


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Concept(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContentConcept(models.Model):
    content = models.ForeignKey('Content')
    concept = models.ForeignKey('Concept')
