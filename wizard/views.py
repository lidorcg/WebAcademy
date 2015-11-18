from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView

from user.views import LoginRequiredMixin
from wizard.models import Tag


# Create your views here.
@login_required()
def wizard_view(request):
    return render(request, 'wizard/wizard.html')


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = ['name']
