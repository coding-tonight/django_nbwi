# Generated by Django 4.2.4 on 2023-10-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_account_reference_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='reference_id',
            field=models.CharField(default='e130a9ec3aed44aaaf93a64818f39809', max_length=32, unique=True),
        ),
    ]
