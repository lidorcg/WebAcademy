from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, DetailView
from syllabus.models import Course
from user.views import LoginRequiredMixin


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'whitenapp/course-list.html'


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'whitenapp/course-download.html'
