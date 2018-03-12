from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Subscriber(models.Model):
    email = models.EmailField()
    email_confirm = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=56, blank=True, null=True, default=None)
    index = models.CharField(max_length=6, blank=True, null=True, default=None)
    street = models.CharField(max_length=30, blank=True, null=True, default=None)
    locality = models.CharField(max_length=10, blank=True, null=True, default=None)
    tel_number = models.CharField(max_length=11, blank=True, null=True, default=None)
    company_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    nip = models.CharField(max_length=10, blank=True, null=True, default=None)
    company_confirm = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return "User %s %s %s %s" % (self.id, self.name, self.email, self.city)

    # def save(self, *args, **kwargs):
    #     email = self.user.email
    #     self.email = email
    #     # self.total_price = int(self.nmb) * price_per_item
    #
    #     super(Subscriber, self).save(*args, **kwargs)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Subscriber.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.subscriber.save()

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'


class LogoImage(models.Model):
    image = models.ImageField(upload_to='logo_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'LogoPhoto'
        verbose_name_plural = 'LogoPhotos'


class SliderMain(models.Model):
    ad_name = models.CharField(max_length=64)
    ad_customer = models.CharField(max_length=64)
    ad_description = models.TextField(blank=True, null=True, default=None)
    ad_title = models.CharField(max_length=128)
    ad_text = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='advert_images/')
    url = models.URLField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    position = models.IntegerField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    activation_date = models.DateField(blank=True, default=None)
    deactivation_date = models.DateField(blank=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'SliderMain'
        verbose_name_plural = 'SliderMains'
