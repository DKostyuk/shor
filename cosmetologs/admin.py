from django.contrib import admin
from .models import *


# class CosmetologCategoryInline(admin.TabularInline):
#     model = CosmetologCategory
#     extra = 0
#
#
# class CosmetologAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in Cosmetolog._meta.fields]
#     prepopulated_fields = {'code': ('name',)}
#     inlines = [CosmetologCategoryInline]
#
#     class Meta:
#         model = Cosmetolog
#
# admin.site.register(Cosmetolog, CosmetologAdmin)

##############################################################################################
# class BlogCategoryAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in BlogCategory._meta.fields]
#
#     class Meta:
#         model = BlogCategory
#
# admin.site.register(BlogCategory, BlogCategoryAdmin)





# class BlogImageAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in BlogImage._meta.fields]
#
#     class Meta:
#         model = BlogImage
#
# admin.site.register(BlogImage, BlogImageAdmin)
