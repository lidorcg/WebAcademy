from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
from django.views.generic import CreateView
from user.views import LoginRequiredMixin
from wizard.models import Course


@login_required()
def wizard_view(request):
    return render(request, 'wizard/wizard.html')


class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['title', 'description', 'prerequisites', 'requirements']
