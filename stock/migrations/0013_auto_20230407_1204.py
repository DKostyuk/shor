# Generated by Django 3.2.11 on 2023-04-07 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220718_1152'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0012_auto_20230330_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitemminus',
            name='due_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.CreateModel(
            name='StockItemReserved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_minus', models.IntegerField(default=0)),
                ('due_date', models.DateField(blank=True, default=None, null=True)),
                ('comments', models.CharField(blank=True, default=None, max_length=124, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.productcategory')),
                ('id_purchase', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_purchase_item_reserved', to='stock.purchaseitem')),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_product_item_reserved', to='products.productitem')),
            ],
            options={
                'verbose_name': 'StockItemReserved',
                'verbose_name_plural': 'StockItemReserved',
            },
        ),
    ]