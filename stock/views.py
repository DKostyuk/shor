from django.shortcuts import render
from blogs.models import *


def blog_item(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except:
        blog = None
    blogs_images_all = BlogImage.objects.filter(is_active=True, is_main=True)
    blogs_images = blogs_images_all[:2]

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
#
#     print (request.session.session_key)
#
    return render(request, 'blogs/blog_item_full.html', locals())


def blog(request, slug=None):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    blog_all = Blog.objects.filter(is_active=True)

    return render(request, 'blogs/blog.html', locals())
