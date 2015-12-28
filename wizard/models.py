from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ShallowCourse(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prerequisites = models.TextField(blank=True)
    requirements = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Concept(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey('Group', null=True, blank=True, default=None)

    def __str__(self):
        return self.name
