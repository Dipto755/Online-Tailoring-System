# Generated by Django 4.2.6 on 2023-10-15 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TailorApp', '0023_remove_measurementforkameez_model_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measureforsalwar_model',
            name='user',
        ),
        migrations.RemoveField(
            model_name='measurementforshirt_model',
            name='user',
        ),
    ]
