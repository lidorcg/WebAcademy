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
from django.contrib.auth import views as auth_views

from user import views

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, name='login-form'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^not-registered/$', views.not_registered_view, name='not-registered'),
    url(r'^not-active/$', views.not_active_view, name='not-active'),
    url(r'^dashboard/$', views.dashboard_view, name='dashboard'),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^settings/$', views.settings_view, name='settings'),
    # REST API for CourseMessage
    url(r'^messages/add/$', views.MessageCreate.as_view(), name='message-add'),
    url(r'^messages/(?P<pk>[0-9]+)/update/$', views.MessageUpdate.as_view(), name='message-update'),
    url(r'^messages/(?P<pk>[0-9]+)/delete/$', views.MessageDelete.as_view(), name='message-delete'),
]
