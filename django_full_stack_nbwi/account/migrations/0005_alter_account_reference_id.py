# Generated by Django 4.2.4 on 2023-10-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_account_reference_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='reference_id',
            field=models.CharField(default='80567d9a6a4c43fbb61e53116fcd562c', max_length=32),
        ),
    ]