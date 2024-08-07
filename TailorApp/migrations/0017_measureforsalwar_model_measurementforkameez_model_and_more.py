# Generated by Django 4.2.6 on 2023-10-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TailorApp', '0016_delete_measureforsalwar_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='measureForSalwar_model',
            fields=[
                ('sl_productID', models.IntegerField(primary_key=True, serialize=False)),
                ('sl_length', models.IntegerField()),
                ('sl_waist_length', models.IntegerField()),
                ('sl_hip_length', models.IntegerField()),
                ('sl_thigh_length', models.IntegerField()),
                ('sl_width', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='measurementForKameez_model',
            fields=[
                ('k_productID', models.IntegerField(primary_key=True, serialize=False)),
                ('k_length', models.IntegerField()),
                ('k_body_length', models.IntegerField()),
                ('k_shoulder_length', models.IntegerField()),
                ('k_waist_length', models.IntegerField()),
                ('k_hip_length', models.IntegerField()),
                ('k_hand_width', models.IntegerField()),
                ('k_neck_length', models.IntegerField()),
                ('k_neck_width', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='measurementForShirt_model',
            fields=[
                ('s_productID', models.IntegerField(primary_key=True, serialize=False)),
                ('s_collar_length', models.IntegerField()),
                ('s_sleeve_length', models.IntegerField()),
                ('s_shoulder_length', models.IntegerField()),
                ('s_bicep', models.IntegerField()),
                ('s_chest_length', models.IntegerField()),
                ('s_hip_length', models.IntegerField()),
            ],
        ),
    ]
