from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


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


def logout_view(request):
    logout(request)
    return redirect('user:login-form')


def not_registered_view(request):
    return render(request, 'user/not-registered.html')


def not_active_view(request):
    return render(request, 'user/not-active.html')


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
