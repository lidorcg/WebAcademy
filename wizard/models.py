from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ShallowCourse(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prerequisites = models.TextField(blank=True)
    requirements = models.TextField(blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
