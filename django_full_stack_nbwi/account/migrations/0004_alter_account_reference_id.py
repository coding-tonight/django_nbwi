# Generated by Django 4.2.5 on 2023-10-03 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_reference_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='reference_id',
            field=models.CharField(default='fdd34e9122a047fe9beff61e5c9812b3', max_length=32),
        ),
    ]
