# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-22 10:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_productinbasket_session_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasket',
            name='order',
        ),
        migrations.RemoveField(
            model_name='productinbasket',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='nmb',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='price_per_item',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='total_price',
        ),
        migrations.DeleteModel(
            name='ProductInBasket',
        ),
    ]
