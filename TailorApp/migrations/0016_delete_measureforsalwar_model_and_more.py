# Generated by Django 4.2.6 on 2023-10-14 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TailorApp', '0015_remove_design_salowaar_model_ds_image2_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='measureForSalwar_model',
        ),
        migrations.DeleteModel(
            name='measurementForKameez_model',
        ),
        migrations.DeleteModel(
            name='measurementForShirt_model',
        ),
    ]
