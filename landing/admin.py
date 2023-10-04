from django.contrib import admin
from .models import *


# class SubscriberAdmin (admin.ModelAdmin):
#     list_display = ['id', "name", "email", 'city']
#     # list_display = [field.name for field in Subscriber._meta.fields]
#     list_filter = ['name', 'city']
#     search_fields = ['name', 'email', 'city']
#     # fields = ["email"]
#     # exclude = ["email"]
#     # inlines = [FieldMappingInline]
# 	# fields = []
#     #exclude = ["type"]
# 	#list_filter = ('report_data',)
# 	# search_fields = ['category', 'subCategory', 'suggestKeyword']
#
#     class Meta:
#         model = Subscriber
#
# admin.site.register(Subscriber, SubscriberAdmin)


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


class LetterAdmin (admin.ModelAdmin):
    list_display = ['type', 'subject', 'from_name', 'email_sender', 'phone_sender', 'city_sender',
                    'msg', 'created', 'updated', 'cosmetolog', 'user_email', 'who_answer']
    readonly_fields = ['type', 'subject', 'email_sender', 'phone_sender', 'cosmetolog',
                       'message', 'created', 'updated', ]
        # list_display = [field.name for field in Letter._meta.fields]

    def msg(self, obj):
        return obj.message[:20]

    class Meta:
        model = Letter


admin.site.register(Letter, LetterAdmin)


class LetterEmailInline(admin.TabularInline):
    model = LetterEmail
    extra = 0


class LetterTemplateAdmin (admin.ModelAdmin):
    list_display = [field.name for field in LetterTemplate._meta.fields]
    inlines = [LetterEmailInline]

    class Meta:
        model = LetterTemplate


admin.site.register(LetterTemplate, LetterTemplateAdmin)


class PageAdmin (admin.ModelAdmin):
    list_display = ['page_name', 'page_text_1', 'is_active']
    # fields = ['activation_date', 'deactivation_date', 'ad_name',
    #           'ad_customer', 'ad_description', 'is_active', 'is_main']

    def page_text_1(self, obj):
        return obj.page_text[:20]

    class Meta:
        model = Page


admin.site.register(Page, PageAdmin)


class TrainingAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Training._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Training


admin.site.register(Training, TrainingAdmin)


class TrainingUserAdmin (admin.ModelAdmin):
    list_display = [field.name for field in TrainingUser._meta.fields]

    class Meta:
        model = TrainingUser


admin.site.register(TrainingUser, TrainingUserAdmin)


# class SubscriberCosmetologAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in SubscriberCosmetolog._meta.fields]
#
#     class Meta:
#         model = SubscriberCosmetolog
#

# admin.site.register(SubscriberCosmetolog, SubscriberCosmetologAdmin)


class FeatureAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Feature._meta.fields]

    class Meta:
        model = Feature


admin.site.register(Feature, FeatureAdmin)
