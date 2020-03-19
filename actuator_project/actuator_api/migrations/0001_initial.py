# Generated by Django 3.0.4 on 2020-03-14 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('modbus_address', models.IntegerField()),
                ('model', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('role', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('actuator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actuator_api.Actuator')),
                ('parameter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actuator_api.Parameter')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.IntegerField()),
                ('log_date', models.DateTimeField(verbose_name='date loged')),
                ('actuator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actuator_api.Actuator')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actuator_api.User')),
            ],
            options={
                'ordering': ['log_date'],
            },
        ),
    ]
