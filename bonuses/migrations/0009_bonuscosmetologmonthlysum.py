# Generated by Django 3.2.11 on 2023-09-13 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetologs', '0001_initial'),
        ('bonuses', '0008_auto_20230908_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusCosmetologMonthlySum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_monthly_sum', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('month_start_date', models.DateField(blank=True, default=None, null=True)),
                ('month_end_date', models.DateField(blank=True, default=None, null=True)),
                ('month_year', models.CharField(blank=True, default=None, max_length=16, null=True)),
                ('cosmetolog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.cosmetolog')),
            ],
            options={
                'verbose_name': 'BonusCosmetologMonthlySum',
                'verbose_name_plural': 'BonusCosmetologMonthlySums',
            },
        ),
    ]
