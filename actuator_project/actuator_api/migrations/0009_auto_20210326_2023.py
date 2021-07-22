# Generated by Django 3.0.4 on 2021-03-27 00:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actuator_api', '0008_auto_20210326_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='actuator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='actuator_api.Actuator'),
        ),
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]