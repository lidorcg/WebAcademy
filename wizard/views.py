from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView

from user.views import LoginRequiredMixin
from wizard.models import Idea, Concept, Group


# Create your views here.
@login_required()
def wizard_view(request):
    return render(request, 'wizard/wizard.html')


class IdeaCreate(LoginRequiredMixin, CreateView):
    model = Idea
    fields = ['user', 'title', 'description']
    success_url = reverse_lazy('wizard:wizard')


class ConceptCreate(LoginRequiredMixin, CreateView):
    model = Concept
    fields = ['name']
    success_url = reverse_lazy('wizard:wizard')


class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name']
    success_url = reverse_lazy('wizard:wizard')
