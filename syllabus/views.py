# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course, Module, Lesson, Unit, LessonType, UnitType
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('course-list')
        else:
            return render(request, 'registration/not-active.html')
    else:
        return render(request, 'registration/not-registered.html')


def logout_view(request):
    logout(request)
    return redirect('login-form')


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


# REST API for course
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'


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
    success_url = reverse_lazy('course-list')


# REST API for module
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
        return reverse_lazy('module-detail', kwargs={'pk': self.get_object().id})


class ModuleDelete(LoginRequiredMixin, DeleteView):
    model = Module

    def get_success_url(self):
        return reverse_lazy('course-detail', kwargs={'pk': self.get_object().course_id})


# REST API for lesson
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
        return reverse_lazy('lesson-detail', kwargs={'pk': self.get_object().id})


class LessonDelete(LoginRequiredMixin, DeleteView):
    model = Lesson

    def get_success_url(self):
        return reverse_lazy('module-detail', kwargs={'pk': self.get_object().module_id})


# Partial Updates
class LessonUpdateDone(LoginRequiredMixin, UpdateView):
    model = Lesson
    fields = ['done']


# REST API for unit
class UnitCreate(LoginRequiredMixin, CreateView):
    model = Unit
    fields = ['lesson', 'order', 'name', 'url', 'type']


class UnitUpdate(LoginRequiredMixin, UpdateView):
    model = Unit
    fields = ['name', 'url', 'type']


class UnitDelete(LoginRequiredMixin, DeleteView):
    model = Unit

    def get_success_url(self):
        return reverse_lazy('lesson-detail', kwargs={'pk': self.get_object().lesson_id})

# ToDo create CRUD views for tags
# ToDo add permissions checks
