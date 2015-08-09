# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Course, Module, Content, Type


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'


class ModuleDetailView(DetailView):
    model = Module
    context_object_name = 'module'


class ContentDetailView(DetailView):
    model = Content
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        context = super(ContentDetailView, self).get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context
