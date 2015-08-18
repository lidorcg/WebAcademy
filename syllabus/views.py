# Create your views here.
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Course, Module, Content, Type


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'


class CourseCreate(CreateView):
    model = Course
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse_lazy('course-detail', kwargs={'pk': self.get_object().id})


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'


class CourseUpdate(UpdateView):
    model = Course
    fields = ['title', 'description', 'prerequisites', 'requirements']

    def get_success_url(self):
        return reverse_lazy('course-detail', kwargs={'pk': self.get_object().id})


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('course-list')


class ModuleCreate(CreateView):
    model = Module
    fields = ['course', 'order', 'title', 'description']

    def get_success_url(self):
        return reverse_lazy('course-detail', kwargs={'pk': self.get_object().course.id})


class ModuleDetailView(DetailView):
    model = Module
    context_object_name = 'module'

    def get_context_data(self, **kwargs):
        context = super(ModuleDetailView, self).get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class ModuleUpdate(UpdateView):
    model = Module
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse_lazy('module-detail', kwargs={'pk': self.get_object().id})


class ModuleDelete(DeleteView):
    model = Module

    def get_success_url(self):
        return reverse_lazy('course-detail', kwargs={'pk': self.get_object().course.id})


class ContentCreate(CreateView):
    model = Content
    fields = ['module', 'title', 'description', 'type', 'order']

    def get_success_url(self):
        return reverse_lazy('module-detail', kwargs={'pk': self.get_object().module.id})


class ContentDetailView(DetailView):
    model = Content
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        context = super(ContentDetailView, self).get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class ContentUpdate(UpdateView):
    model = Content
    fields = ['title', 'description', 'type', 'time', 'requirements']

    def get_success_url(self):
        return reverse_lazy('content-detail', kwargs={'pk': self.get_object().id})


class ContentDelete(DeleteView):
    model = Content

    def get_success_url(self):
        return reverse_lazy('module-detail', kwargs={'pk': self.get_object().module.id})

# ToDo create CRUD views for concepts
