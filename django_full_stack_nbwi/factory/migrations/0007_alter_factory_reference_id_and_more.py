# Generated by Django 4.2.4 on 2023-10-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0006_alter_factory_reference_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='reference_id',
            field=models.CharField(default='717e89df70b947acb06c81d67cdf78a2', max_length=32),
        ),
        migrations.AlterField(
            model_name='factoryowner',
            name='reference_id',
            field=models.CharField(default='717e89df70b947acb06c81d67cdf78a2', max_length=32),
        ),
    ]