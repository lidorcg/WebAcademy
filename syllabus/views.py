# Create your views here.
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Course, Module, Lesson, Unit, LessonType, UnitType


# ToDo add login view

# REST API for course
class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'


class CourseCreate(CreateView):
    model = Course
    fields = ['title', 'description']


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'


class CourseUpdate(UpdateView):
    model = Course
    fields = ['title', 'description', 'prerequisites', 'requirements']


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('course-list')


# REST API for module
class ModuleCreate(CreateView):
    model = Module
    fields = ['course', 'order', 'title', 'description']


class ModuleDetailView(DetailView):
    model = Module
    context_object_name = 'module'

    def get_context_data(self, **kwargs):
        context = super(ModuleDetailView, self).get_context_data(**kwargs)
        context['lesson_types'] = LessonType.objects.all()
        return context


class ModuleUpdate(UpdateView):
    model = Module
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse_lazy('module-detail', kwargs={'pk': self.get_object().id})


class ModuleDelete(DeleteView):
    model = Module

    def get_success_url(self):
        return reverse_lazy('course-detail', kwargs={'pk': self.get_object().course_id})


# REST API for lesson
class LessonCreate(CreateView):
    model = Lesson
    fields = ['module', 'title', 'description', 'type', 'order']


class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        context['lesson_types'] = LessonType.objects.all()
        context['unit_types'] = UnitType.objects.all()
        return context


class LessonUpdate(UpdateView):
    model = Lesson
    fields = ['title', 'description', 'type', 'time', 'requirements']

    def get_success_url(self):
        return reverse_lazy('lesson-detail', kwargs={'pk': self.get_object().id})


class LessonDelete(DeleteView):
    model = Lesson

    def get_success_url(self):
        return reverse_lazy('module-detail', kwargs={'pk': self.get_object().module_id})


# Partial Updates
class LessonUpdateDone(UpdateView):
    model = Lesson
    fields = ['done']


# REST API for unit
class UnitCreate(CreateView):
    model = Unit
    fields = ['lesson', 'order', 'name', 'url', 'type']


class UnitUpdate(UpdateView):
    model = Unit
    fields = ['name', 'url', 'type']


class UnitDelete(DeleteView):
    model = Unit

    def get_success_url(self):
        return reverse_lazy('lesson-detail', kwargs={'pk': self.get_object().lesson_id})


# ToDo create CRUD views for tags

