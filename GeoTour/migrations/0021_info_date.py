# Generated by Django 4.1.6 on 2023-02-03 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoTour', '0020_alter_info_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
