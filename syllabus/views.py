from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Course, Module, Content


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
