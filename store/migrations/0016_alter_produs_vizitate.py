# Generated by Django 3.2 on 2021-04-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_produs_vizitate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produs',
            name='vizitate',
            field=models.CharField(blank=True, choices=[('Cel mai vizitat', 'celmaivizitat')], max_length=50, null=True),
        ),
    ]
