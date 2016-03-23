from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from syllabus.models import Course, Module, Lesson, LessonType
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


def done_view(request):
    idea = Idea.objects.filter(user__id=request.user.id).first()
    crs = Course.objects.create(title=idea.title, description=idea.description)
    crs.instructors.add(request.user)
    Module.objects.create(course=crs, order=crs.get_modules_count(), title="Introduction")
    for grp in idea.group_set.all():
        mdl = Module.objects.create(course=crs, order=crs.get_modules_count(), title=grp.name)
        lsn_typ = LessonType.objects.get(pk=1)
        Lesson.objects.create(module=mdl, order=mdl.get_lessons_count(), title="Intro", type=lsn_typ)
        for cpt in grp.concept_set.all():
            Lesson.objects.create(module=mdl, order=mdl.get_lessons_count(), title=cpt.name, type=lsn_typ)
        Lesson.objects.create(module=mdl, order=mdl.get_lessons_count(), title="Summary", type=lsn_typ)
    Module.objects.create(course=crs, order=crs.get_modules_count(), title="Conclusion")
    idea.delete()
    return HttpResponseRedirect(reverse_lazy('syllabus:course-detail', kwargs={'pk': crs.id}))
