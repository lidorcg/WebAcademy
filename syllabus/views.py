# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Course, Module, Content, Concept, Type


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'


class ModuleDetailView(DetailView):
    model = Module
    context_object_name = 'module'


class ContentDetailView(DetailView):
    model = Content
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        context = super(ContentDetailView, self).get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


from rest_framework import viewsets
from syllabus.serializers import CourseSerializer, ModuleSerializer, ContentSerializer, ConceptSerializer, TypeSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows modules to be viewed or edited.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ContentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contents to be viewed or edited.
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ConceptViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows concepts to be viewed or edited.
    """
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer


class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows types to be viewed or edited.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer