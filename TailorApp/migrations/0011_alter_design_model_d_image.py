# Generated by Django 4.2.6 on 2023-10-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TailorApp', '0010_alter_fabric_model_f_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design_model',
            name='d_image',
            field=models.ImageField(default='', upload_to='design/images'),
        ),
    ]