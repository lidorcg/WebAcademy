import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebAcademy.settings")

from datetime import timedelta
import random

from syllabus.models import LessonType, UnitType

LessonType(name='Learn', icon='school').save()
LessonType(name='Practice', icon='assignment').save()
LessonType(name='Test', icon='spellcheck').save()

UnitType(name='Video', icon='videocam').save()
UnitType(name='Document', icon='description').save()
UnitType(name='Image', icon='image').save()
UnitType(name='Website', icon='public').save()
UnitType(name='Audio', icon='audiotrack').save()
UnitType(name='Software', icon='sd_card').save()
UnitType(name='File', icon='insert_drive_file').save()

from syllabus.models import Course, Module, Lesson, Unit

c = Course(title='Demo',
           description='This is a sample course to show all the options this system holds.').save()

for i in range(5):
    m = Module(course=c,
               order=i,
               title='M' + str(i),
               description='This is a module(kind of a chapter) in the course.').save()

    for j in range(5):
        l = Lesson(module=m,
                   order=j,
                   title='L' + str(j),
                   description="""This is a lesson in the course.
                   A lesson may introduce to the module, deliver one main subject or a few small related subjects,
                   practice the learned subjects, present a test or summarize the module.""",
                   type=LessonType.objects.get(j % LessonType.objects.count()),
                   time=timedelta(hours=random.randint(0, 3), minutes=random.randint(0, 60))).save()

        for k in range(5):
            u = Unit(lesson=l,
                     order=k,
                     name='U' + str(k),
                     type=UnitType.objects.get(j % UnitType.objects.count()),
                     url='http://www.sample.com/' + 'Unit' + str(k)).save()
