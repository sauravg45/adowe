# Generated by Django 2.0.9 on 2018-12-20 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='no_of_cars',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
