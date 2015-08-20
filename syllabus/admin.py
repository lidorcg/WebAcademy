from django.contrib import admin

from .models import Course, Module, Lesson, Tag, Type


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


admin.site.register(Lesson)
admin.site.register(Tag)
admin.site.register(Type)
