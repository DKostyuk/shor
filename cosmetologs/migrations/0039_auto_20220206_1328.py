# Generated by Django 3.2.11 on 2022-02-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetologs', '0038_auto_20220206_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cosmetolog',
            old_name='cosmetolog_surmname',
            new_name='cosmetolog_name',
        ),
        migrations.RemoveField(
            model_name='cosmetolog',
            name='name',
        ),
        migrations.AddField(
            model_name='cosmetolog',
            name='cosmetolog_surname',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]