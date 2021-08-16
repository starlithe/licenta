# Generated by Django 3.1.4 on 2021-08-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment',
            field=models.CharField(choices=[('PR1', '12:00-13:00'), ('PR2', '13:00-14:00'), ('PR3', '14:00-15:00'), ('PR4', '15:00-16:00'), ('PR5', '16:00-17:00'), ('PR6', '17:00-18:00')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='appointment',
            name='day',
            field=models.CharField(choices=[('Lun', 'Luni'), ('Mar', 'Marti '), ('Mie', 'Miercuri'), ('Joi', 'Joi'), ('Vin', 'Vineri'), ('Sam', 'Sambata'), ('Dum', 'Duminica')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='appointment',
            name='frizer',
            field=models.CharField(choices=[('FR1', 'Claudiu'), ('FR2', 'Ivanciu'), ('FR3', 'Gheorghe')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='appointment',
            name='pachet',
            field=models.CharField(choices=[('PAC1', 'Tuns'), ('PAC2', 'Tuns + Barba'), ('PAC3', 'Tuns + Barba + Aranjat'), ('PAC4', 'Barba'), ('PAC5', 'Vopsit barba'), ('PAC6', 'Pensat')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]
