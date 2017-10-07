from django.contrib import admin
from .models import *


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 0


class BlogCategoryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in BlogCategory._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = BlogCategory

admin.site.register(BlogCategory, BlogCategoryAdmin)


class BlogAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Blog._meta.fields]
    prepopulated_fields = {'slug': ('title_name',)}
    inlines = [BlogImageInline]

    class Meta:
        model = Blog

admin.site.register(Blog, BlogAdmin)


class BlogImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in BlogImage._meta.fields]

    class Meta:
        model = BlogImage

admin.site.register(BlogImage, BlogImageAdmin)
