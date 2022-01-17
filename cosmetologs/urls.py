"""test_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from django.contrib import admin
from cosmetologs import views

urlpatterns = [
    # url(r'^landing/', views.landing, name='landing'),
    re_path(r'^cosmetolog/(?P<slug>[\w-]+)/$', views.cosmetolog, name='cosmetolog'),
    # url(r'^service/(?P<slug1>[\w-]+)/(?P<slug>[\w-]+)/$', views.service, name='service'),
    re_path(r'^service/(?P<slug2>[\w-]+)/(?P<slug1>[\w-]+)/(?P<slug>[\w-]+)/$', views.service, name='service'),
]
