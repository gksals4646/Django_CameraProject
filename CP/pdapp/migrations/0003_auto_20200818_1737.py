# Generated by Django 3.1 on 2020-08-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdapp', '0002_auto_20200811_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='countbuy',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pdsale',
            field=models.IntegerField(null=True),
        ),
    ]
