from django.views.generic import CreateView, ListView, DetailView, UpdateView

from user.views import LoginRequiredMixin
from wizard.models import Idea, Concept, Group


# Create your views here.

class Step1View(LoginRequiredMixin, ListView):
    # ToDo make sure there is only one idea per user
    model = Idea
    context_object_name = 'idea'
    template_name = 'wizard/step-1.html'

    def get_queryset(self):
        return Idea.objects.filter(user__id=self.request.user.id).first()


class Step2View(LoginRequiredMixin, DetailView):
    model = Idea
    context_object_name = 'idea'
    template_name = 'wizard/step-2.html'


class Step3View(LoginRequiredMixin, DetailView):
    model = Idea
    context_object_name = 'idea'
    template_name = 'wizard/step-3.html'


class IdeaCreate(LoginRequiredMixin, CreateView):
    model = Idea
    fields = ['user', 'title', 'description']


class ConceptCreate(LoginRequiredMixin, CreateView):
    model = Concept
    fields = ['idea', 'name']


class ConceptUpdate(LoginRequiredMixin, UpdateView):
    model = Concept
    fields = ['group']


class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['idea', 'name']
