# Generated by Django 3.2.11 on 2022-02-14 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0034_auto_20220214_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='cosmetolog_email',
        ),
    ]