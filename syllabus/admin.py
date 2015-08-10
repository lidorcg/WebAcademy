from django.contrib import admin

from .models import Course, Module, Content, Concept, Type


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


admin.site.register(Content)
admin.site.register(Concept)
admin.site.register(Type)
