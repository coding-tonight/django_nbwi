# Generated by Django 4.2.4 on 2023-10-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_alter_item_reference_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='reference_id',
            field=models.CharField(default='d508fb5136a64cdf9de74e4c66069c01', max_length=32),
        ),
    ]
