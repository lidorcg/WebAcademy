from django.contrib import admin

from .models import Course, Module, Content, Concept, Type, ContentConcept


# Register your models here.
class ModuleInline(admin.TabularInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline, ]


class ContentInline(admin.StackedInline):
    model = Content
    extra = 0


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ContentInline, ]


class ContentConceptInline(admin.StackedInline):
    model = ContentConcept


@admin.register(Content)
class LectureAdmin(admin.ModelAdmin):
    inlines = [ContentConceptInline, ]


admin.site.register(Concept)
admin.site.register(Type)
