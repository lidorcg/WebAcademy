from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Course


class Index(ListView):
    model = Course
    context_object_name = 'courses'
