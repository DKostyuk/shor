# Generated by Django 3.2.11 on 2022-01-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetologs', '0035_auto_20191112_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cosmetolog',
            name='active_until',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='city_cosmetolog',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='description',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='description_product',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='description_region',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='description_service',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='description_tariff',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='fee',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='headline',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='house_cosmetolog',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='index_cosmetolog',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='logo_image',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='order_email',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='order_nmb',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='order_phone',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='registration_time',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='review_count',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='site_url',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='street_cosmetolog',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='type_text',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='working_hours',
        ),
        migrations.AddField(
            model_name='cosmetolog',
            name='certificate_image',
            field=models.ImageField(default=None, upload_to='certificate_images/'),
        ),
        migrations.AddField(
            model_name='cosmetolog',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=16, null=True),
        ),
    ]