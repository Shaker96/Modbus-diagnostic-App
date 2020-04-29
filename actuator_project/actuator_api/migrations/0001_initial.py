# Generated by Django 3.0.4 on 2020-04-24 00:45

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'SuperAdmin'), (1, 'Admin'), (2, 'Regular')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, 'Active'), (1, 'Inactive')])),
                ('modbus_address', models.SmallIntegerField(unique=True)),
                ('model', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading_date', models.DateTimeField(auto_now=True)),
                ('raw_data', models.CharField(default='error', max_length=200)),
                ('response_ok', models.BooleanField(default=False)),
                ('actuator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actuator_api.Actuator')),
            ],
            options={
                'ordering': ['reading_date'],
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_number', models.SmallIntegerField()),
                ('description', models.CharField(max_length=200)),
                ('bit_number', models.SmallIntegerField(null=True)),
                ('min_value', models.SmallIntegerField(null=True)),
                ('max_value', models.SmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('reading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actuator_api.Reading')),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actuator_api.Register')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=200)),
                ('log_date', models.DateTimeField(auto_now=True)),
                ('actuator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='actuator_api.Actuator')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['log_date'],
            },
        ),
        migrations.CreateModel(
            name='ActuatorAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actuator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actuator_api.Actuator')),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actuator_api.Register')),
            ],
        ),
    ]
