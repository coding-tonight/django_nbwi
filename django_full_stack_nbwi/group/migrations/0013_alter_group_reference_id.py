# Generated by Django 4.2.4 on 2023-10-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0012_alter_group_reference_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='reference_id',
            field=models.UUIDField(default='ce17f931fba3493182a7a8fe7593086e', unique=True),
        ),
    ]