# Generated by Django 4.2.4 on 2023-10-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0009_factoryowner_opening_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='reference_id',
            field=models.CharField(default='7a15973e69c140278c210690695cb572', max_length=32),
        ),
        migrations.AlterField(
            model_name='factoryowner',
            name='reference_id',
            field=models.CharField(default='7a15973e69c140278c210690695cb572', max_length=32),
        ),
    ]
