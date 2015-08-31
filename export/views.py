# Create your views here.
from django.views.generic import ListView, DetailView

from syllabus.models import Course, Module, Lesson, Unit
from user.views import LoginRequiredMixin


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'export/list-view.html'


class CourseScriptView(LoginRequiredMixin, DetailView):
    model = Course
    context_object_name = 'course'
    content_type = 'text/plain'
    template_name = 'export/scripts/base-script'


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'export/list-view.html'


class ModuleScriptView(LoginRequiredMixin, DetailView):
    model = Module
    context_object_name = 'course'
    content_type = 'text/plain'
    template_name = 'export/scripts/base-script'


class ModuleDetailView(LoginRequiredMixin, DetailView):
    model = Module
    context_object_name = 'module'
    template_name = 'export/list-view.html'


class LessonScriptView(LoginRequiredMixin, DetailView):
    model = Lesson
    context_object_name = 'lesson'
    content_type = 'text/plain'
    template_name = 'export/scripts/base-script'


class LessonDetailView(LoginRequiredMixin, DetailView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'export/list-view.html'


class UnitScriptView(LoginRequiredMixin, DetailView):
    model = Unit
    context_object_name = 'unit'
    content_type = 'text/plain'
    template_name = 'export/scripts/base-script'
