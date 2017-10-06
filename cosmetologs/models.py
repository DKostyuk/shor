# from django.db import models
# from django.contrib.auth.models import User
#
#
# class CategoryForCosmetolog(models.Model):
#     name = models.CharField(max_length=32, blank=True, null=True, default=None)
#     # code = models.SlugField(max_length=32, unique=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return "%s" % self.name
#
#     class Meta:
#         verbose_name = 'CategoryForCosmetolog'
#         verbose_name_plural = 'CategoriesForCosmetolog'
#
#
# class Cosmetolog(models.Model):
#     name = models.CharField(max_length=128, blank=True, null=True, default=None)
#     code = models.SlugField(max_length=128, unique=True)
#     order_email = models.EmailField()
#     order_phone = models.CharField(max_length=10, blank=True, null=True, default=None)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     logo_image = models.ImageField(upload_to='logo_images/')
#     description = models.CharField(max_length=255, blank=True, null=True, default=None)
#     description_region = models.CharField(max_length=255, blank=True, null=True, default=None)
#     description_tariff = models.CharField(max_length=255, blank=True, null=True, default=None)
#     headline = models.CharField(max_length=128, blank=True, null=True, default=None)
#     rating = models.DecimalField(max_digits=3, decimal_places=0, default=0)
#     review_count = models.IntegerField(default=0)
#     order_nmb = models.IntegerField(default=0)
#     fee = models.DecimalField(max_digits=3, decimal_places=2, default=0)
#     is_active = models.BooleanField(default=False)
#     is_visible = models.BooleanField(default=False)
#     registration_time = models.DateTimeField(blank=True, default=None)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     site_url = models.URLField()
#     active_until = models.DateTimeField(auto_now_add=True, auto_now=False)
#     is_paid = models.BooleanField(default=False)
#     modified_by = models.ForeignKey(User, blank=True, null=True, default=None)
#
#     def __str__(self):
#         return "%s" % self.name
#         # return "%s, %s" % (self.price, self.name)
#
#     class Meta:
#         verbose_name = 'Cosmetolog'
#         verbose_name_plural = 'Cosmetologs'
#
#
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
#     # code = models.SlugField(max_length=64, unique=True)
#     price01 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     price02 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     price_avg = models.DecimalField(max_digits=10, decimal_places=2, default=0) #(price01+price02)/2
#     price_action = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     discount = models.IntegerField(default=0)
#     category = models.ForeignKey(CategoryForCosmetolog, blank=True, null=True, default=None)
#     description = models.TextField(blank=True, null=True, default=None)
#     short_description = models.TextField(blank=True, null=True, default=None)
#     is_active = models.BooleanField(default=True)
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
# class ServiceImage(models.Model):
#     service = models.ForeignKey(ServiceProduct, blank=True, null=True, default=None)
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
#         verbose_name = 'ServicePhoto'
#         verbose_name_plural = 'ServicePhotos'
