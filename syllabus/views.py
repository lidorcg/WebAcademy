# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from user.views import LoginRequiredMixin
from .models import Course, Module, Lesson, Unit, LessonType, UnitType


# REST API for Course
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Course.objects.all()
        else:
            return Course.objects.filter(instructors__id=self.request.user.id)


class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['title', 'description']


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    context_object_name = 'course'


class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['title', 'description', 'prerequisites', 'requirements']


class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('syllabus:course-list')


# Partial Updates
def modules_reorder(request, pk):
    new_order = request.POST.getlist('order[]')
    for idx, item in enumerate(new_order):
        m = Module.objects.get(pk=item)
        m.order = idx
        m.save()
    return HttpResponse()


# REST API for Module
class ModuleCreate(LoginRequiredMixin, CreateView):
    model = Module
    fields = ['course', 'order', 'title', 'description']


class ModuleDetailView(LoginRequiredMixin, DetailView):
    model = Module
    context_object_name = 'module'

    def get_context_data(self, **kwargs):
        context = super(ModuleDetailView, self).get_context_data(**kwargs)
        context['lesson_types'] = LessonType.objects.all()
        return context


class ModuleUpdate(LoginRequiredMixin, UpdateView):
    model = Module
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse_lazy('syllabus:module-detail', kwargs={'pk': self.get_object().id})


class ModuleDelete(LoginRequiredMixin, DeleteView):
    model = Module

    def get_success_url(self):
        return reverse_lazy('syllabus:course-detail', kwargs={'pk': self.get_object().course_id})


# Partial Updates
def lessons_reorder(request, pk):
    # ToDo fix lesson reordering
    new_order = request.POST['order']
    for idx, item in enumerate(new_order):
        l = Lesson.objects.get(pk=item)
        l.order = idx
        l.save()
    return HttpResponse()


# REST API for Lesson
class LessonCreate(LoginRequiredMixin, CreateView):
    model = Lesson
    fields = ['module', 'title', 'description', 'type', 'order']


class LessonDetailView(LoginRequiredMixin, DetailView):
    model = Lesson
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        context['lesson_types'] = LessonType.objects.all()
        context['unit_types'] = UnitType.objects.all()
        return context


class LessonUpdate(LoginRequiredMixin, UpdateView):
    model = Lesson
    fields = ['title', 'description', 'type', 'time', 'requirements']

    def get_success_url(self):
        return reverse_lazy('syllabus:lesson-detail', kwargs={'pk': self.get_object().id})


class LessonDelete(LoginRequiredMixin, DeleteView):
    model = Lesson

    def get_success_url(self):
        return reverse_lazy('syllabus:module-detail', kwargs={'pk': self.get_object().module_id})


# Partial Updates
class LessonUpdateDone(LoginRequiredMixin, UpdateView):
    model = Lesson
    fields = ['done']


def units_reorder(request, pk):
    # ToDo fix unit reordering
    new_order = request.POST['order']
    for idx, item in enumerate(new_order):
        u = Unit.objects.get(pk=item)
        u.order = idx
        u.save()
    return HttpResponse()


# REST API for Unit
class UnitCreate(LoginRequiredMixin, CreateView):
    model = Unit
    fields = ['lesson', 'order', 'name', 'url', 'type']


class UnitDelete(LoginRequiredMixin, DeleteView):
    model = Unit

    def get_success_url(self):
        return reverse_lazy('syllabus:lesson-detail', kwargs={'pk': self.get_object().lesson_id})
