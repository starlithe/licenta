# Generated by Django 3.1.4 on 2021-08-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_appointment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]