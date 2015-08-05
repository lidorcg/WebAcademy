from django.contrib import admin

from .models import Course, Module, Lecture, Assignment, Quiz, Concept
from .models import LectureConcept, AssignmentConcept, QuizConcept


# Register your models here.
admin.site.register(Concept)


class ModuleInline(admin.TabularInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline, ]


class LectureInline(admin.TabularInline):
    model = Lecture


class AssignmentInline(admin.TabularInline):
    model = Assignment


class QuizInline(admin.TabularInline):
    model = Quiz


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [LectureInline, AssignmentInline, QuizInline, ]


class LectureConceptInline(admin.TabularInline):
    model = LectureConcept


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    inlines = [LectureConceptInline, ]


class AssignmentConceptInline(admin.TabularInline):
    model = AssignmentConcept


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    inlines = [AssignmentConceptInline, ]


class QuizConceptInline(admin.TabularInline):
    model = QuizConcept


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuizConceptInline, ]
