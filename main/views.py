from django.shortcuts import redirect


# Create your views here.

def index(request):
    if request.user is not None:
        if request.user.is_active:
            return redirect('syllabus:course-list')
        else:
            return redirect('user:not-active')
    else:
        return redirect('user:login-form')
