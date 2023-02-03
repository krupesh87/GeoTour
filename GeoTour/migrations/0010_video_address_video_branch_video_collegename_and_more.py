# Generated by Django 4.1.6 on 2023-02-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoTour', '0009_delete_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='branch',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='collegename',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='establishin',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='information',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='otherfaculty',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]