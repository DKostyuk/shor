# Generated by Django 3.2.11 on 2023-03-11 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20220718_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockItemPlus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_purchase', models.CharField(blank=True, default=None, max_length=16, null=True)),
                ('num_plus', models.IntegerField(default=0)),
                ('price_plus_usd', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price_plus_uah', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('due_date', models.DateField(blank=True, default=None, null=True)),
                ('comments', models.CharField(blank=True, default=None, max_length=124, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_product_item', to='products.productitem')),
            ],
            options={
                'verbose_name': 'StockItemPlus',
                'verbose_name_plural': 'StockItemPluses',
            },
        ),
        migrations.CreateModel(
            name='StockFilePlus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, default=None, max_length=124, null=True)),
                ('stock_file', models.FileField(blank=True, default=None, null=True, upload_to='stock_file_add/')),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'StockFilePlus',
                'verbose_name_plural': 'StockFilePluses',
            },
        ),
    ]
