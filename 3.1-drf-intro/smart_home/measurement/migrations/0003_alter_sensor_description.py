# Generated by Django 5.0 on 2024-01-17 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_options_alter_sensor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='Описание'),
        ),
    ]
