# Generated by Django 3.2.11 on 2022-08-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_productinbasket_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='user',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]