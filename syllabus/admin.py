from django.contrib import admin

from .models import Course, Module, Content, Concept, ContentConcept


# Register your models here.
class ModuleInline(admin.TabularInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline, ]


class ContentInline(admin.TabularInline):
    model = Content
    extra = 0


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ContentInline, ]


class ContentConceptInline(admin.TabularInline):
    model = ContentConcept


@admin.register(Content)
class LectureAdmin(admin.ModelAdmin):
    inlines = [ContentConceptInline, ]


admin.site.register(Concept)