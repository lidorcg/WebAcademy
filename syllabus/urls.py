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
    url(r'login/', views.login_view, name='login'),
    url(r'logout/', views.logout_view, name='logout'),
    url(r'^$', views.CourseListView.as_view(), name='home'),
    # REST API for course
    url(r'^courses/$', views.CourseListView.as_view(), name='course-list'),
    url(r'^courses/add/$', views.CourseCreate.as_view(), name='course-add'),
    url(r'^courses/(?P<pk>[0-9]+)/$', views.CourseDetailView.as_view(), name='course-detail'),
    url(r'^courses/(?P<pk>[0-9]+)/update/$', views.CourseUpdate.as_view(), name='course-update'),
    url(r'^courses/(?P<pk>[0-9]+)/delete/$', views.CourseDelete.as_view(), name='course-delete'),
    # REST API for module
    url(r'^courses/(?P<pk>[0-9]+)/modules/add/$', views.ModuleCreate.as_view(), name='module-add'),
    url(r'^modules/(?P<pk>[0-9]+)/$', views.ModuleDetailView.as_view(), name='module-detail'),
    url(r'^modules/(?P<pk>[0-9]+)/update/$', views.ModuleUpdate.as_view(), name='module-update'),
    url(r'^modules/(?P<pk>[0-9]+)/delete/$', views.ModuleDelete.as_view(), name='module-delete'),
    # REST API for lesson
    url(r'^modules/(?P<pk>[0-9]+)/lessons/add/$', views.LessonCreate.as_view(), name='lesson-add'),
    url(r'^lessons/(?P<pk>[0-9]+)/$', views.LessonDetailView.as_view(), name='lesson-detail'),
    url(r'^lessons/(?P<pk>[0-9]+)/update/$', views.LessonUpdate.as_view(), name='lesson-update'),
    url(r'^lessons/(?P<pk>[0-9]+)/delete/$', views.LessonDelete.as_view(), name='lesson-delete'),
    # Partial Updates
    url(r'^lessons/(?P<pk>[0-9]+)/update-done/$', views.LessonUpdateDone.as_view(), name='lesson-update-done'),
    # REST API for unit
    url(r'^lessons/(?P<pk>[0-9]+)/units/add/$', views.UnitCreate.as_view(), name='unit-add'),
    url(r'^units/(?P<pk>[0-9]+)/update/$', views.UnitUpdate.as_view(), name='unit-update'),
    url(r'^units/(?P<pk>[0-9]+)/delete/$', views.UnitDelete.as_view(), name='unit-delete'),
]

# ToDo create CRUD urls for Tags
