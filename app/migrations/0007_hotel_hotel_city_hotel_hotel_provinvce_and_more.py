# Generated by Django 4.1.7 on 2023-03-25 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_hotel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_provinvce',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
