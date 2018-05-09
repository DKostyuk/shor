from django.db import models
from addresses.models import Address
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
# from django.utils import timezone
from django.utils.text import slugify
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


def subcategory_category_creator(self,*args, **kwargs):
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


class Cosmetolog(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=128, unique=True)
    order_email = models.EmailField()
    order_phone = models.CharField(max_length=10, blank=True, null=True, default=None)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    logo_image = models.ImageField(upload_to='logo_images/')
    description = models.CharField(max_length=255, blank=True, null=True, default=None)
    description_region = models.CharField(max_length=255, blank=True, null=True, default=None)
    description_tariff = models.CharField(max_length=255, blank=True, null=True, default=None)
    headline = models.CharField(max_length=128, blank=True, null=True, default=None)
    rating = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    review_count = models.IntegerField(default=0)
    order_nmb = models.IntegerField(default=0)
    fee = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    is_active = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)
    registration_time = models.DateTimeField(blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    site_url = models.URLField()
    active_until = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_paid = models.BooleanField(default=False)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.name
        # return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Cosmetolog'
        verbose_name_plural = 'Cosmetologs'


class CosmetologCategory(models.Model):
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryForCosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategoryForCosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
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
    price_avg = models.DecimalField(max_digits=10, decimal_places=2, default=0) #(price01+price02)/2
    price_action = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryForCosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategoryForCosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        # return "%s" % self.name
        return "%s, %s" % (self.price_avg, self.name)

    class Meta:
        verbose_name = 'ServiceProduct'
        verbose_name_plural = 'ServiceProducts'


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


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Cosmetolog.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        # instance.slug = unique_slug_generator(instance)


# pre_save.connect(pre_save_post_receiver, sender=CategoryForCosmetolog)
pre_save.connect(pre_save_post_receiver, sender=Cosmetolog)
# pre_save.connect(pre_save_post_receiver, sender=ServiceProduct)


class CosmetologAddress(models.Model):
    cosmetolog_name = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    cosmetolog_id = models.IntegerField(blank=True, null=True, default=None)
    address_name = models.ForeignKey(Address, blank=True, null=True, default=None, on_delete=models.CASCADE)
    address_id = models.IntegerField(blank=True, null=True, default=None)
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

        super(CosmetologAddress, self).save(*args, **kwargs)
