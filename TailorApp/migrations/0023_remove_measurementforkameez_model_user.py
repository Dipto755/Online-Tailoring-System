# Generated by Django 4.2.6 on 2023-10-15 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TailorApp', '0022_alter_measurementforkameez_model_k_productid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurementforkameez_model',
            name='user',
        ),
    ]
