# Generated by Django 4.2.5 on 2023-10-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_item_reference_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='reference_id',
            field=models.CharField(default='a6a7584871a6410693fbff204186d718', max_length=32),
        ),
    ]
