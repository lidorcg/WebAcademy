# Create your models here.

from django.contrib.auth.models import User
from django.db import models
from syllabus.models import Course, Module, Lesson


class Message(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course, blank=True, null=True)
    module = models.ForeignKey(Module, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, blank=True, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
