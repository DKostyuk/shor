"""b_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
# from search import views as search_views


urlpatterns = [
    # url(r'^ckeditor/', include('ckeditor.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('landing.urls')),
    re_path(r'^', include('products.urls')),
    re_path(r'^', include('orders.urls')),
    re_path(r'^', include('blogs.urls')),
    re_path(r'^', include('cosmetologs.urls')),
    re_path(r'^', include('addresses.urls')),
    re_path(r'^', include('another.urls')),
    # url(r'^search/', search_views.search, name='search'),
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
