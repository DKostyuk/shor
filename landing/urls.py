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
from django.conf.urls import url, include
from django.contrib import admin
from landing import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^landing/$', views.landing, name='landing'),

    url(r'^uslugi-kosmetyczne/$', views.salon, name='salon'),

    url(r'^uslugi-kosmetyczne/(?P<q_1>[\w-]+)/$', views.search_service_address, name='search_service_address'),
    url(r'^uslugi-kosmetyczne/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/$', views.search_service_address,
        name='search_service_address'),
    url(r'^uslugi-kosmetyczne/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/(?P<q_3>[\w-]+)/$',
        views.search_service_address, name='search_search_service'),
    url(r'^uslugi-kosmetyczne/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/(?P<q_3>[\w-]+)/(?P<q_4>[\w-]+)/$',
        views.search_service_address, name='search_search_service'),

    url(r'^service-in-Poland/(?P<q1>[\w-]+)/$', views.search_service, name='search_service'),
    url(r'^service-in-Poland/(?P<q1>[\w-]+)/(?P<q2>[\w-]+)/$', views.search_service, name='search_service'),
    url(r'^service-in-Poland/(?P<q1>[\w-]+)/(?P<q2>[\w-]+)/(?P<q3>[\w-]+)/$', views.search_service,
        name='search_service'),

    url(r'^cosmetolog-in/(?P<q1>[\w-]+)/$', views.search_address, name='search_address'),
    url(r'^cosmetolog-in/(?P<q1>[\w-]+)/(?P<q2>[\w-]+)/$', views.search_address, name='search_address'),
    url(r'^cosmetolog-in/(?P<q1>[\w-]+)/(?P<q2>[\w-]+)/(?P<q3>[\w-]+)/$', views.search_address, name='search_address'),


    # url(r'^salon/(?P<query1>[\w-]+)/(?P<query>[\w-]+)/$', views.salon, name='salon'),
]
