from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.db import models

from syllabus.models import Course, Module, Lesson


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course, blank=True, null=True)
    module = models.ForeignKey(Module, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, blank=True, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        if self.course:
            return reverse_lazy('syllabus:course-detail', args=[str(self.course_id)])
        if self.module:
            return reverse_lazy('syllabus:module-detail', args=[str(self.module_id)])
        if self.lesson:
            return reverse_lazy('syllabus:lesson-detail', args=[str(self.lesson_id)])
