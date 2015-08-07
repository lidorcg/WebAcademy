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
    url(r'^courses/$', views.CourseListView.as_view(), name='course-list'),
    url(r'^courses/(?P<pk>[0-9]+)/$', views.CourseDetailView.as_view(), name='course-detail'),
    url(r'^modules/(?P<pk>[0-9]+)/$', views.ModuleDetailView.as_view(), name='module-detail'),
    url(r'^contents/(?P<pk>[0-9]+)/$', views.ContentDetailView.as_view(), name='content-detail'),
    url(r'^$', views.CourseListView.as_view(), name='home'),
]
