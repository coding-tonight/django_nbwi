# Generated by Django 4.2.5 on 2023-10-03 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='reference_id',
            field=models.CharField(default='c88960ebd2ee418abc725c8a09b611e7', max_length=32),
        ),
    ]
