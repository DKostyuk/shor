from django.db import models
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
# from django.utils import timezone
from django.utils.text import slugify
# from django.utils import unique_slug_generator


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


def full_address_creator(self,*args, **kwargs):
    s = list()
    s.append(self.name)
    parent_id = self.parent_id.id
    while parent_id is not None:
        address_set = Address.objects.filter(id=parent_id)
        for i in address_set:
            s.append(i.name)
        if i.parent_id is None:
            parent_id = None
        else:
            parent_id = i.parent_id.id
    s = list(reversed(s))
    full = ''
    for j in range(len(s)):
        d = s[j].encode('utf8')
        if j != len(s) - 1:
            full += d + ', '
        else:
            full += d
    return full


def display_address_creator(self,*args, **kwargs):
    s = list()
    s.append(self.name)
    parent_id = self.parent_id.id
    type_id = self.type_id
    print(type_id)
    print(type(type_id))
    while parent_id is not None:
        address_set = Address.objects.filter(id=parent_id)
        for i in address_set:
            print(i.type_id)
            print(type(i.type_id))
            if type_id in (0, 1, 2, 3, 4):
                break
            elif type_id == 10 and i.type_id == 5:
                s.append(i.name)
                break
            elif type_id == 10 and i.type_id != 5:
                continue
            else:
                s.append(i.name)
        if i.parent_id is None:
            parent_id = None
        else:
            parent_id = i.parent_id.id
    s = list(reversed(s))
    full = ''
    for j in range(len(s)):
        d = s[j].encode('utf8')
        if j != len(s) - 1:
            full += d + ', '
        else:
            full += d
    return full


class Address(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=32, unique=True)
    full_address = models.CharField(max_length=256, blank=True, null=True, default=None)
    display_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    url = models.CharField(max_length=128, blank=True, null=True, default=None)
    parent_id = models.ForeignKey('self', null=True, blank=True)
    type_id = models.IntegerField(blank=True, null=True, default=None)
    type_level = models.ForeignKey(AddressType, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        # return "%s" % self.id
        return "%s, %s" % (self.id, self.name)

    def __unicode__(self):
        return "%s" % self.id
        # return "%s, %s" % (self.id, self.name)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'

    def save(self, *args, **kwargs):
        # self.display_address = str(Address.objects.filter(id=1)) + ','
        # p1 = self.parent_id
        # p = p1.name
        # print(999)
        # print(p)
        # print(111111)
        self.display_address = display_address_creator(self)
        self.type_id = self.type_level.level
        self.full_address = full_address_creator(self)
        # price_per_item = self.product.price
        # self.price_per_item = price_per_item
        # self.total_price = int(self.nmb) * price_per_item

        super(Address, self).save(*args, **kwargs)


# class CosmetologCategory(models.Model):
#     cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None)
#     category = models.ForeignKey(CategoryForCosmetolog, blank=True, null=True, default=None)
#     is_active = models.BooleanField(default=True)
#     is_main = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#         return "%s" % self.id
#
#     class Meta:
#         verbose_name = 'CosmetologCategory'
#         verbose_name_plural = 'CosmetologCategories'
#
#
# class ServiceProduct(models.Model):
#     name = models.CharField(max_length=64, blank=True, null=True, default=None)
#     slug = models.SlugField(max_length=64, unique=True)
#     price01 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     price02 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     price_avg = models.DecimalField(max_digits=10, decimal_places=2, default=0) #(price01+price02)/2
#     price_action = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     discount = models.IntegerField(default=0)
#     cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None)
#     category = models.ForeignKey(CategoryForCosmetolog, blank=True, null=True, default=None)
#     description = models.TextField(blank=True, null=True, default=None)
#     short_description = models.TextField(blank=True, null=True, default=None)
#     is_active = models.BooleanField(default=True)
#     is_visible = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     modified_by = models.ForeignKey(User, blank=True, null=True, default=None)
#
#     def __str__(self):
#         # return "%s" % self.name
#         return "%s, %s" % (self.price_avg, self.name)
#
#     class Meta:
#         verbose_name = 'ServiceProduct'
#         verbose_name_plural = 'ServiceProducts'
#
#
# class ServiceProductImage(models.Model):
#     service_product = models.ForeignKey(ServiceProduct, blank=True, null=True, default=None)
#     image = models.ImageField(upload_to='products_images/')
#     is_active = models.BooleanField(default=True)
#     is_main = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#         return "%s" % self.id
#
#     class Meta:
#         verbose_name = 'ServiceProductPhoto'
#         verbose_name_plural = 'ServiceProductPhotos'

#####################################################################

# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.name)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Cosmetolog.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" % (slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
#
#
# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#         # instance.slug = unique_slug_generator(instance)
#
#
# # pre_save.connect(pre_save_post_receiver, sender=CategoryForCosmetolog)
# pre_save.connect(pre_save_post_receiver, sender=Cosmetolog)
# # pre_save.connect(pre_save_post_receiver, sender=ServiceProduct)
