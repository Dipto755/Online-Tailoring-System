# Generated by Django 4.2.6 on 2023-10-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TailorApp', '0009_fabric_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabric_model',
            name='f_image',
            field=models.ImageField(default='', upload_to='fabric/images'),
        ),
    ]