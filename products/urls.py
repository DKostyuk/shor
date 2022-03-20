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
from products import views

urlpatterns = [
    re_path(r'^ingredient/(?P<slug>[\w-]+)/$', views.ingredient, name='ingredient'),
    re_path(r'^ingredient/', views.ingredient_no, name='ingredient_no'),
    re_path(r'^product/(?P<slug>[\w-]+)/$', views.product, name='product'),
    re_path(r'^product/', views.product_no, name='product_no'),
    # re_path(r'^product/(?P<slug1>[\w-]+)/(?P<slug>[\w-]+)/$', views.product, name='product'),
    re_path(r'^product_line/(?P<slug>[\w-]+)/$', views.product_line, name='product_line'),
    re_path(r'^product_line/', views.product_line, name='product_line'),
    # url(r'^product_line/(?P<slug1>[\w-]+)/(?P<slug>[\w-]+)/$', views.product_line, name='product_line'),
]
# url(r'^landing/', views.landing, name='landing'),
