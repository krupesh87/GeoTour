# Generated by Django 4.1.6 on 2023-02-02 12:44

import GeoTour.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoTour', '0017_alter_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.CharField(default=GeoTour.models.create_id, editable=False, max_length=1000, primary_key=True, serialize=False),
        ),
    ]