# Generated by Django 3.2.11 on 2022-02-14 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0033_delete_lettertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='user_name',
        ),
    ]