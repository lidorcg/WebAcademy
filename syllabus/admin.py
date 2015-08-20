from django.contrib import admin

from .models import Course, Module, Lesson, Unit, Tag, LessonType, UnitType


# Register your models here.
class ModuleInline(admin.TabularInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline, ]


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [LessonInline, ]


class UnitInline(admin.TabularInline):
    model = Unit
    extra = 0


@admin.register(Lesson)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [UnitInline, ]


admin.site.register(Unit)
admin.site.register(Tag)
admin.site.register(LessonType)
admin.site.register(UnitType)

