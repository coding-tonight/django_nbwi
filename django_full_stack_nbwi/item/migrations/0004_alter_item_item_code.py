# Generated by Django 4.2.5 on 2023-10-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_item_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
