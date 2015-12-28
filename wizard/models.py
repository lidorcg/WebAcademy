from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Idea(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Group(models.Model):
    course = models.ForeignKey('Idea', null=True, blank=True, default=None)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Concept(models.Model):
    group = models.ForeignKey('Group', null=True, blank=True, default=None)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
