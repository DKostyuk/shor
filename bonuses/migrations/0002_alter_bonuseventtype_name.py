# Generated by Django 3.2.11 on 2023-08-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonuses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonuseventtype',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=16, null=True),
        ),
    ]
