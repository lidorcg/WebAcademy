from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView

from user.models import Message


# Create your views here.

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('syllabus:course-list')
        else:
            return redirect('user:not-active')
    else:
        return redirect('user:not-registered')


# ToDo delete session after logout
@login_required()
def logout_view(request):
    logout(request)
    return redirect('user:login-form')


def not_registered_view(request):
    return render(request, 'registration/not-registered.html')


def not_active_view(request):
    return render(request, 'registration/not-active.html')


@login_required()
def dashboard_view(request):
    return render(request, 'user/dashboard.html')


@login_required()
def profile_view(request):
    return render(request, 'user/profile.html')


@login_required()
def settings_view(request):
    return render(request, 'user/settigns.html')


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


# REST API for Course
class MessageCreate(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['user', 'course', 'module', 'lesson', 'text']


class MessageUpdate(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ['text']


class MessageDelete(LoginRequiredMixin, DeleteView):
    model = Message

    def get_success_url(self):
        return self.get_object().get_absolute_url()
