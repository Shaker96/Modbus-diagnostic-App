# Generated by Django 3.0.4 on 2021-03-27 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actuator_api', '0006_auto_20200522_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='event',
            field=models.SmallIntegerField(choices=[(0, 'El usuario ha iniciado sesión'), (1, 'El usuario ha cerrado sesión'), (2, 'Se ha creado un nuevo usuario'), (3, 'Un actuador ha sido operado manualmente'), (4, 'Nueva lectura disponible')]),
        ),
    ]