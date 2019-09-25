from django.db import models
# from landing.models import Subscriber
from addresses.models import Address
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from b_project.current_user import get_current_user
from ckeditor.fields import RichTextField
import openpyxl
# from django.utils import timezone
# from django.utils.text import slugify
from uuslug import slugify
# from django.utils import unique_slug_generator


class CategoryForCosmetolog(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=32, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'CategoryForCosmetolog'
        verbose_name_plural = 'CategoriesForCosmetolog'


def subcategory_category_creator(self):
    subcategory_category = self.name + ', ' + self.category.name
    url = self.category.slug + '/' + self.slug

    return subcategory_category, url


class SubCategoryForCosmetolog(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=32, unique=True)
    category = models.ForeignKey(CategoryForCosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    subcategory_category = models.CharField(max_length=64, blank=True, null=True, default=None)
    url = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        # return "%s" % self.name
        return "%s, %s" % (self.name, self.category)

    def __unicode__(self):
        # return "%s" % self.name
        return "%s, %s, %s" % (self.name, self.category, self.url)

    class Meta:
        verbose_name = 'SubCategoryForCosmetolog'
        verbose_name_plural = 'SubCategoriesForCosmetolog'

    def save(self, *args, **kwargs):
        self.subcategory_category, self.url = subcategory_category_creator(self)

        super(SubCategoryForCosmetolog, self).save(*args, **kwargs)


class CosmetologType(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=32, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'CosmetologType'
        verbose_name_plural = 'CosmetologTypes'


class Cosmetolog(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=128, unique=True)
    type = models.ForeignKey(CosmetologType, blank=True, null=True, default=None, on_delete=models.CASCADE)
    city_cosmetolog = models.ForeignKey(Address, blank=True, null=True, default=None, on_delete=models.CASCADE)
    index_cosmetolog = models.CharField(max_length=5, blank=True, null=True, default=None)
    street_cosmetolog = models.ForeignKey(Address, related_name='street_cosmetolog', blank=True, null=True, default=None, on_delete=models.CASCADE)
    house_cosmetolog = models.CharField(max_length=8, blank=True, null=True, default=None)
    order_email = models.EmailField(blank=True, null=True, default=None)
    order_phone = models.CharField(max_length=13, blank=True, null=True, default=None)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    logo_image = models.ImageField(upload_to='logo_images/', help_text="optimal size  600x450")
    description = RichTextField(blank=True, null=True, default=None,
                                help_text="краткое описание, 70 симоволов, которых будет на шот-рекламе")
    description_region = models.CharField(max_length=255, blank=True, null=True, default=None)
    description_tariff = models.CharField(max_length=255, blank=True, null=True, default=None)
    description_service = models.CharField(max_length=255, blank=True, null=True, default=None)
    description_product = models.CharField(max_length=255, blank=True, null=True, default=None)
    headline = models.CharField(max_length=128, blank=True, null=True, default=None)
    working_hours = models.CharField(max_length=128, blank=True, null=True, default=None)
    rating = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    review_count = models.IntegerField(default=0)
    order_nmb = models.IntegerField(default=0)
    fee = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    is_active = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)
    registration_time = models.DateTimeField(blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    site_url = models.URLField(blank=True, null=True, default=None)
    active_until = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_paid = models.BooleanField(default=False)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        # return "%s" % self.name
        return "%s, %s" % (self.id, self.name)

    class Meta:
        verbose_name = 'Cosmetolog'
        verbose_name_plural = 'Cosmetologs'


class CosmetologEmail(models.Model):
    email = models.EmailField(blank=True, null=True, default=None)
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.email

    class Meta:
        verbose_name = 'CosmetologEmail'
        verbose_name_plural = 'CosmetologEmails'


class CosmetologPhone(models.Model):
    phone = models.CharField(max_length=10, blank=True, null=True, default=None)
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.phone

    class Meta:
        verbose_name = 'CosmetologPhone'
        verbose_name_plural = 'CosmetologPhones'


class CosmetologCategory(models.Model):
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryForCosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategoryForCosmetolog, blank=True, null=True, default=None,
                                    on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'CosmetologCategory'
        verbose_name_plural = 'CosmetologCategories'


class ServiceProduct(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=64, unique=True)
    price01 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price02 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_avg = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # (price01+price02)/2
    price_action = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryForCosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategoryForCosmetolog, blank=True, null=True, default=None,
                                    on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        # return "%s" % self.name
        return "%s, %s" % (self.id, self.name)

    class Meta:
        verbose_name = 'ServiceProduct'
        verbose_name_plural = 'ServiceProducts'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user
            # if not self.id:
            #     self.created_by = user
        super(ServiceProduct, self).save(*args, **kwargs)


class ServiceProductImage(models.Model):
    service_product = models.ForeignKey(ServiceProduct, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'ServiceProductPhoto'
        verbose_name_plural = 'ServiceProductPhotos'


def create_slug(sender, instance):
    print(123456789, sender)
    slug = slugify(instance.name)
    qs = sender.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        last = sender.objects.last()
        new_slug = "%s-%s" % (slug, last.id)
        return new_slug
    else:
        return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(sender, instance)
        # instance.slug = unique_slug_generator(instance)


# pre_save.connect(pre_save_post_receiver, sender=CategoryForCosmetolog)
pre_save.connect(pre_save_post_receiver, sender=Cosmetolog)
pre_save.connect(pre_save_post_receiver, sender=ServiceProduct)


class CosmetologAddress(models.Model):
    cosmetolog_name = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    cosmetolog_id = models.IntegerField(blank=True, null=True, default=None)
    service_name = models.ForeignKey(ServiceProduct, blank=True, null=True, default=None, on_delete=models.CASCADE)
    service_id = models.IntegerField(blank=True, null=True, default=None)
    address_name = models.ForeignKey(Address, blank=True, null=True, default=None, on_delete=models.CASCADE)
    address_id = models.IntegerField(blank=True, null=True, default=None)
    address_type_id = models.IntegerField(blank=True, null=True, default=None)
    city_id = models.IntegerField(blank=True, null=True, default=-1)
    district_id = models.IntegerField(blank=True, null=True, default=-1)
    street_id = models.IntegerField(blank=True, null=True, default=-1)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'CosmetologAddress'
        verbose_name_plural = 'CosmetologAddresses'

    def save(self, *args, **kwargs):
        self.cosmetolog_id = self.cosmetolog_name_id
        self.address_id = self.address_name_id
        self.service_id = self.service_name_id
        print(9999, self.address_name.type_id)
        self.address_type_id = self.address_name.type_id
        if self.address_type_id == 10:
            self.street_id = self.address_id
            self.district_id = self.address_name.parent_id.id
            print(1234, self.address_name.parent_id.parent_id.id)
            print(1234, type(self.address_name.parent_id.parent_id.id))
            self.city_id = self.address_name.parent_id.parent_id.id
        elif self.address_type_id == 5:
            self.district_id = self.address_type_id
        # self.city_id = 4

        super(CosmetologAddress, self).save(*args, **kwargs)
