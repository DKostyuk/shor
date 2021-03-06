
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
from orders import views

urlpatterns = [
   re_path(r'^basket_adding/', views.basket_adding, name='basket_adding'),
   re_path(r'^checkout/', views.checkout, name='checkout'),
   re_path(r'^basket_update/', views.basket_update, name='basket_update'),
   re_path(r'^order_history/', views.order_history, name='order_history'),
]