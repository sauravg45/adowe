# Generated by Django 2.0.9 on 2018-12-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oda', '0005_brand_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pos_data',
            name='latpos',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pos_data',
            name='lonpos',
            field=models.FloatField(),
        ),
    ]
