from django.shortcuts import render
from blogs.models import *


def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    blogs_images_all = BlogImage.objects.filter(is_active=True, is_main=True)
    blogs_images = blogs_images_all[:2]

#     session_key = request.session.session_key
#     if not session_key:
#         request.session.cycle_key()
#
#     print (request.session.session_key)
#
    return render(request, 'blogs/blog.html', locals())
