from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView
from syllabus.models import Course
from user.views import LoginRequiredMixin


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
