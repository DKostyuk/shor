from django.contrib import admin
from .models import *


class SubscriberAdmin (admin.ModelAdmin):
    list_display = ['id', "name", "email", 'city']
    # list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name', 'city']
    search_fields = ['name', 'email', 'city']
    # fields = ["email"]
    # exclude = ["email"]
    # inlines = [FieldMappingInline]
	# fields = []
    #exclude = ["type"]
	#list_filter = ('report_data',)
	# search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)


class LogoImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in LogoImage._meta.fields]

    class Meta:
        model = LogoImage

admin.site.register(LogoImage, LogoImageAdmin)


class SliderMainAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SliderMain._meta.fields]
    # fields = ['activation_date', 'deactivation_date', 'ad_name',
    #           'ad_customer', 'ad_description', 'is_active', 'is_main']

    class Meta:
        model = SliderMain

admin.site.register(SliderMain, SliderMainAdmin)
