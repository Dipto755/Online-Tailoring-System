# Generated by Django 4.2.6 on 2023-10-15 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TailorApp', '0028_alter_kameez_order_model_o_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kameez_order_model',
            name='user',
        ),
        migrations.RemoveField(
            model_name='salowaar_order_model',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shirt_order_model',
            name='user',
        ),
    ]
