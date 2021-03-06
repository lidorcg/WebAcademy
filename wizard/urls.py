"""syllabus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from wizard import views

urlpatterns = [
    url(r'^step1/$', views.Step1View.as_view(), name='step-1'),
    url(r'^step2/(?P<pk>[0-9]+)/$', views.Step2View.as_view(), name='step-2'),
    url(r'^step3/(?P<pk>[0-9]+)/$', views.Step3View.as_view(), name='step-3'),
    url(r'^ideas/add/$', views.IdeaCreate.as_view(), name='idea-add'),
    url(r'^concepts/add/$', views.ConceptCreate.as_view(), name='concept-add'),
    url(r'^concepts/(?P<pk>[0-9]+)/update/$', views.ConceptUpdate.as_view(), name='concept-update'),
    url(r'^groups/add/$', views.GroupCreate.as_view(), name='group-add'),
    url(r'^done/$', views.done_view, name='done'),
]
