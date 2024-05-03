# Generated by Django 3.2.11 on 2023-04-07 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20220718_1152'),
        ('stock', '0014_auto_20230407_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockItemRest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_rest', models.IntegerField(default=0)),
                ('due_date', models.DateField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.productcategory')),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_product_item_rest', to='products.productitem')),
            ],
            options={
                'verbose_name': 'StockItemRest',
                'verbose_name_plural': 'StockItemRest',
            },
        ),
    ]