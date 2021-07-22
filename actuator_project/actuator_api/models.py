from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class CustomUser(AbstractUser):
    SUPERUSER = 0
    ADMIN = 1
    REGULAR = 2

    ROLES = (
        (SUPERUSER, 'Superuser'),
        (ADMIN, 'Admin'),
        (REGULAR, 'Regular'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLES)
    idn = models.PositiveIntegerField(unique=True, validators=[
            MaxValueValidator(150000000),
            MinValueValidator(1)
        ])
    def __str__(self):
        return str(self.username)

# python manage.py loaddata registers
class Register(models.Model):
    register_number = models.SmallIntegerField()
    description = models.CharField(max_length=200)
    bit_number = models.SmallIntegerField(null = True)
    min_value = models.SmallIntegerField(null = True)
    max_value = models.SmallIntegerField(null = True)
    unit = models.CharField(max_length=10, null = True)

    def __str__(self):
        return self.description

class Actuator(models.Model):
    ACTIVE = 0
    INACTIVE = 1

    STATUS = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')
    )

    status = models.SmallIntegerField(choices=STATUS)
    modbus_address = models.SmallIntegerField(unique=True)
    model = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Reading(models.Model):
    actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    raw_data = models.CharField(max_length=200, default='error')
    response_ok = models.BooleanField(default=False)
    # class Meta:
    #     ordering = ['-date']
    def __str__(self):
        return str(self.date)

class Value(models.Model):
    register = models.ForeignKey(Register, on_delete=models.CASCADE)
    reading = models.ForeignKey(Reading, on_delete=models.CASCADE)
    value = models.IntegerField()
    alert = models.BooleanField(default=False)
    alert_seen = models.BooleanField(default=False)
    def __str__(self):
        return str(self.register) + ' - Valor: ' + str(self.value)


class Log(models.Model):
    LOGIN = 0
    LOGOUT = 1
    SIGNUP = 2
    ACTUATOR = 3
    READING = 4
    READINGS = 5
    OFFLINE = 6

    EVENTS = (
        (LOGIN, 'El usuario ha iniciado sesión'),
        (LOGOUT, 'El usuario ha cerrado sesión'),
        (SIGNUP, 'Se ha creado un nuevo usuario'),
        (ACTUATOR, 'Un actuador ha sido operado manualmente'),
        (READING, 'Nueva lectura disponible'),
        (READINGS, 'El usuario accedió a las lecturas del actuador'),
        (OFFLINE, 'El actuador se encuentra desconectado')
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null= True, blank= True)
    actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE, null = True, blank= True)
    event = models.SmallIntegerField(choices=EVENTS)
    log_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-log_date']

    def str(self):
        return self.get_description_display()

# class ActuatorAlert(models.Model):
#     value = models.ForeignKey(Value, on_delete=models.CASCADE)
#     def __str__(self):
#         return str(self.value) + ' Actuador: ' + str(self.value.reading.actuator)