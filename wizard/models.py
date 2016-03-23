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

    def get_concepts(self):
        return self.concept_set.all()

    def get_groups(self):
        return self.group_set.all()


class Group(models.Model):
    idea = models.ForeignKey('Idea')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wizard:step-3', args=[str(self.idea_id)])

    def get_concepts(self):
        return self.concept_set.all()


class Concept(models.Model):
    idea = models.ForeignKey('Idea')
    group = models.ForeignKey('Group', null=True, blank=True, default=None)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wizard:step-2', args=[str(self.idea_id)])
