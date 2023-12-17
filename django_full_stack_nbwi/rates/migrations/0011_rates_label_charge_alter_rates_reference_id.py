# Generated by Django 4.2.4 on 2023-10-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0010_alter_rates_reference_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='rates',
            name='label_charge',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='rates',
            name='reference_id',
            field=models.CharField(default='0d62dc69d14c4428a50e40b6a0190862', max_length=32),
        ),
    ]
