import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebAcademy.settings")

from datetime import timedelta
import random

from syllabus.models import LessonType, UnitType

from syllabus.models import Course, Module, Lesson, Unit

c = Course(title='Demo',
           description='This is a sample course to show all the options this system holds.')
c.save()

for i in range(1, 5):
    m = Module(course=c,
               order=i,
               title='M' + str(i),
               description='This is a module(kind of a chapter) in the course.')
    m.save()

    for j in range(1, 5):
        l = Lesson(module=m,
                   order=j,
                   title='L' + str(j),
                   description="""This is a lesson in the course.
                   A lesson may introduce to the module, deliver one main subject or a few small related subjects,
                   practice the learned subjects, present a test or summarize the module.""",
                   type=LessonType.objects.get(pk=random.randint(0, 2)),
                   time=timedelta(hours=random.randint(0, 3), minutes=random.randint(0, 60)))
        l.save()

        for k in range(1, 5):
            u = Unit(lesson=l,
                     order=k,
                     name='U' + str(k),
                     type=UnitType.objects.get(pk=random.randint(0, 6)),
                     url='http://www.sample.com/' + 'Unit' + str(k)).save()
