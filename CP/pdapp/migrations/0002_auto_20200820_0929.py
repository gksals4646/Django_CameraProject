# Generated by Django 3.1 on 2020-08-20 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bodytype',
        ),
        migrations.RemoveField(
            model_name='product',
            name='lenstype',
        ),
        migrations.AddField(
            model_name='product',
            name='pdtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pdapp.type'),
        ),
    ]
