# Generated by Django 3.2.11 on 2023-08-28 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonuses', '0002_alter_bonuseventtype_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bonusaccountcosmetolog',
            options={'verbose_name': 'BonusAccountCosmetolog', 'verbose_name_plural': 'BonusAccountCosmetologs'},
        ),
        migrations.RenameField(
            model_name='bonusaccountcosmetolog',
            old_name='category',
            new_name='cosmetolog',
        ),
    ]
