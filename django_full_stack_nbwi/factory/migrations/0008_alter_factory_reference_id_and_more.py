# Generated by Django 4.2.4 on 2023-10-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0007_alter_factory_reference_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='reference_id',
            field=models.CharField(default='d508fb5136a64cdf9de74e4c66069c01', max_length=32),
        ),
        migrations.AlterField(
            model_name='factoryowner',
            name='reference_id',
            field=models.CharField(default='d508fb5136a64cdf9de74e4c66069c01', max_length=32),
        ),
    ]
