"""user URL Configuration

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
from whitenapp import views

urlpatterns = [
    url(r'^courses/$', views.CourseListView.as_view(), name='course-list'),
    url(r'^courses/(?P<pk>[0-9]+)/script$', views.CourseScriptView.as_view(), name='course-script'),

    url(r'^courses/(?P<pk>[0-9]+)$', views.CourseDetailView.as_view(), name='module-list'),
    url(r'^modules/(?P<pk>[0-9]+)/script$', views.ModuleScriptView.as_view(), name='module-script'),

    url(r'^modules/(?P<pk>[0-9]+)$', views.ModuleDetailView.as_view(), name='lesson-list'),
    url(r'^lessons/(?P<pk>[0-9]+)/script$', views.LessonScriptView.as_view(), name='lesson-script'),

    url(r'^lessons/(?P<pk>[0-9]+)$', views.LessonDetailView.as_view(), name='unit-list'),
    url(r'^units/(?P<pk>[0-9]+)/script$', views.UnitScriptView.as_view(), name='unit-script'),
]