# Generated by Django 3.0.4 on 2020-05-09 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actuator_api', '0002_register_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='alert',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ActuatorAlert',
        ),
    ]
