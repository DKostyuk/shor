from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
from django.utils.text import slugify
# from django.utils import unique_slug_generator
import openpyxl
from unidecode import unidecode
# import codecs


class AddressType(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=32, unique=True)
    variants = models.CharField(max_length=128, blank=True, null=True, default=None)
    level = models.IntegerField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name
        # return "%s, %s" % (self.id, self.name)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'AddressType'
        verbose_name_plural = 'AddressTypes'


def full_address_creator(self):
    s = list()
    parent_id = self.parent_id.id
    if self.type_level:
        if self.type_level.level in (0, 4):
            s.append(self.name)
        else:
            s.append(self.name + ' ' + self.type_level.name)
        while parent_id is not None:
            address_set = Address.objects.filter(id=parent_id)
            for i in address_set:
                if i.type_level.level in (0, 4):
                    s.append(i.name)
                else:
                    s.append(i.name + ' ' + i.type_level.name)
            if i.parent_id is None:
                parent_id = None
            else:
                parent_id = i.parent_id.id
        s = list(reversed(s))
        full = ''
        for j in range(len(s)):
            d = s[j]
            if j != len(s) - 1:
                full += d + ', '
            else:
                full += d
    else:
        address_obj = Address.objects.get(id=parent_id)
        full = address_obj.full_address + ', ' + self.name
    return full


def display_address_creator(self):
    parent_id = self.parent_id.id
    type_id = self.type_id
    s = list()
    if type_id:
        if type_id in (1, 5, 10):
            s.append(self.name + ' ' + self.type_level.name)
        else:
            s.append(self.name)
        while parent_id is not None:
            address_set = Address.objects.filter(id=parent_id)
            for i in address_set:
                if type_id in (10, 5) and i.type_id == 4:
                    s.append(i.name)
                    break
                elif type_id in (10, 5) and i.type_id == 5:
                    s.append(i.name + ' ' + i.type_level.name)
                    break
                elif type_id in (10, 5) and i.type_id != 4:
                    continue
                if type_id in (0, 1, 2, 3, 4):
                    break
                else:
                    s.append(i.name)
            if i.parent_id is None:
                parent_id = None
            else:
                parent_id = i.parent_id.id
        s = list(reversed(s))
        display = ''
        url_display = ''
        for j in range(len(s)):
            d = s[j]
            u = slugify(unidecode(d))
            url_display += '/' + u
            if j != len(s) - 1:
                display += d + ', '
            else:
                display += d
    else:
        address_obj = Address.objects.get(id=parent_id)
        display = address_obj.display_address + ', ' + self.name
        url_display = address_obj.url + "/" + slugify(unidecode(self.name))
    return display, url_display


class Address(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, default=None)
    # slug = models.SlugField(max_length=32, unique=True)
    full_address = models.CharField(max_length=256, blank=True, null=True, default=None)
    display_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    url = models.CharField(max_length=128, blank=True, null=True, default=None)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    type_id = models.IntegerField(blank=True, null=True, default=None)
    type_level = models.ForeignKey(AddressType, blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.name
        # return "%s, %s, %s" % (self.id, self.name, self.url)

    def __unicode__(self):
        # return "%s" % self.name
        return "%s, %s, %s" % (self.id, self.name, self.url)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'

    def save(self, *args, **kwargs):
        if self.type_level:
            self.type_id = self.type_level.level
        self.full_address = full_address_creator(self)
        self.display_address, self.url = display_address_creator(self)

        super(Address, self).save(*args, **kwargs)


class AddressAddFile(models.Model):
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    address_file = models.FileField(upload_to='address_file_add/')
    is_active = models.BooleanField(default=False)
    start_import = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id
        # return "%s, %s" % (self.price_avg, self.name)

    def __unicode__(self):
        return "%s" % self.id
        # return "%s, %s" % (self.price_avg, self.name)

    class Meta:
        verbose_name = 'AddressAddFile'
        verbose_name_plural = 'AddressAddFiles'

    def save(self, *args, **kwargs):
        file_opened = openpyxl.load_workbook(filename=self.address_file)
        active_sheet = file_opened.active
        data_file = active_sheet.values
        data_file = list(data_file)
        for i in range(1, len(data_file)):
            q = data_file[i][1]
            w = AddressType.objects.get(name=data_file[i][2])
            t = Address.objects.get(id=data_file[i][0])
            p = Address(name=q, type_level=w, parent_id=t, is_active=True)
            p.save()

        super(AddressAddFile, self).save(*args, **kwargs)
