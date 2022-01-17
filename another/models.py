from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from schedule.models.events import EventManager


# class EventCalendar(models.Model):
#     event_name = models.CharField(max_length=64)
#     event_start = models.DateTimeField(auto_now=False)
#     event_finish = models.DateTimeField(auto_now=False)
#     is_active = models.BooleanField(default=False)
#     event_description = models.TextField(blank=True, null=True, default=None)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#         return "%s" % self.id
#
#     class Meta:
#         verbose_name = 'EventCalendar'
#         verbose_name_plural = 'EventCalendars'


class ProductFileCSV(models.Model):
    file_name = models.CharField(max_length=64)
    document = models.FileField(upload_to='another_documents/')
    is_active = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'ProductFileCSV'
        verbose_name_plural = 'ProductFileCSVs'


class AnotherTrick(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    is_active = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'AnotherTrick'
        verbose_name_plural = 'AnotherTrick'


class TestEditor(models.Model):
    comments = RichTextField(blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'TestEditor'
        verbose_name_plural = 'TestEditors'


class CalendarTraining(models.Model):
    calendar_name = models.CharField(max_length=64)
    date_picked_from = models.DateTimeField(auto_now=False)
    date_picked_until = models.DateTimeField(auto_now=False)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'CalendarTraining'
        verbose_name_plural = 'CalendarTraining'
