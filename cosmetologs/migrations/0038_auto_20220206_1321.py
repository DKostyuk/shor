# Generated by Django 3.2.11 on 2022-02-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetologs', '0037_cosmetolog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cosmetolog',
            name='cosmetolog_father_name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='cosmetolog',
            name='cosmetolog_surmname',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='cosmetolog',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='cosmetolog',
            name='tel_number',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cosmetolog',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]