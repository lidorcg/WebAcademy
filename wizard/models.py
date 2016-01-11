from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.

class Idea(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wizard:step-2', args=[str(self.id)])


class Group(models.Model):
    idea = models.ForeignKey('Idea')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Concept(models.Model):
    idea = models.ForeignKey('Idea')
    group = models.ForeignKey('Group', null=True, blank=True, default=None)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
