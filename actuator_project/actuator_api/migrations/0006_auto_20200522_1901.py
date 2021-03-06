# Generated by Django 3.0.4 on 2020-05-22 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actuator_api', '0005_customuser_idn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Superuser'), (1, 'Admin'), (2, 'Regular')], default=0),
            preserve_default=False,
        ),
    ]
