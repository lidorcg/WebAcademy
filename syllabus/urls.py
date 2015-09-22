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

from syllabus import views

urlpatterns = [
    # REST API for Course
    url(r'^courses/$', views.CourseListView.as_view(), name='course-list'),
    url(r'^courses/add/$', views.CourseCreate.as_view(), name='course-add'),
    url(r'^courses/(?P<pk>[0-9]+)/$', views.CourseDetailView.as_view(), name='course-detail'),
    url(r'^courses/(?P<pk>[0-9]+)/update/$', views.CourseUpdate.as_view(), name='course-update'),
    url(r'^courses/(?P<pk>[0-9]+)/delete/$', views.CourseDelete.as_view(), name='course-delete'),
    # Partial Updates
    url(r'^courses/(?P<pk>[0-9]+)/reorder/$', views.modules_reorder, name='modules-reorder'),
    # REST API for Module
    url(r'^courses/(?P<pk>[0-9]+)/modules/add/$', views.ModuleCreate.as_view(), name='module-add'),
    url(r'^modules/(?P<pk>[0-9]+)/$', views.ModuleDetailView.as_view(), name='module-detail'),
    url(r'^modules/(?P<pk>[0-9]+)/update/$', views.ModuleUpdate.as_view(), name='module-update'),
    url(r'^modules/(?P<pk>[0-9]+)/delete/$', views.ModuleDelete.as_view(), name='module-delete'),
    # Partial Updates
    url(r'^modules/(?P<pk>[0-9]+)/reorder/$', views.lessons_reorder, name='lessons-reorder'),
    # REST API for Lesson
    url(r'^modules/(?P<pk>[0-9]+)/lessons/add/$', views.LessonCreate.as_view(), name='lesson-add'),
    url(r'^lessons/(?P<pk>[0-9]+)/$', views.LessonDetailView.as_view(), name='lesson-detail'),
    url(r'^lessons/(?P<pk>[0-9]+)/update/$', views.LessonUpdate.as_view(), name='lesson-update'),
    url(r'^lessons/(?P<pk>[0-9]+)/delete/$', views.LessonDelete.as_view(), name='lesson-delete'),
    # Partial Updates
    url(r'^lessons/(?P<pk>[0-9]+)/reorder/$', views.units_reorder, name='units-reorder'),
    url(r'^lessons/(?P<pk>[0-9]+)/update-done/$', views.LessonUpdateDone.as_view(), name='lesson-update-done'),
    # REST API for Unit
    url(r'^lessons/(?P<pk>[0-9]+)/units/add/$', views.UnitCreate.as_view(), name='unit-add'),
    url(r'^units/(?P<pk>[0-9]+)/delete/$', views.UnitDelete.as_view(), name='unit-delete'),
]

# ToDo create CRUD views for Tags
