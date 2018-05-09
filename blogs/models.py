from django.db import models
from django.contrib.auth.models import User


class BlogCategory(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=32, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'CategoryBlog'
        verbose_name_plural = 'CategoryBlogs'


class Blog(models.Model):
    title_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=128, unique=True)
    h1 = models.CharField(max_length=128, blank=True, null=True, default=None)
    category = models.ForeignKey(BlogCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    content_text = models.TextField(blank=True, null=True, default=None)
    main_short_content = models.TextField(blank=True, null=True, default=None)
    main_short_content_01 = models.TextField(blank=True, null=True, default=None)
    main_short_content_02 = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    creator = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.title_name
        # return "%s, %s" % (self.price, self.name)

    def __unicode__(self):
        return "%s" % self.title_name

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blogs_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Blog_Photo'
        verbose_name_plural = 'Blog_Photos'
