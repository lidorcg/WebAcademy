import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebAcademy.settings")

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
