from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    ADMIN = 0
    REGULAR = 1

    ROLES = (
        (ADMIN, 'Admin'),
        (REGULAR, 'Regular'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLES, blank=True, null=True)
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
    def __str__(self):
        return str(self.register) + ' - Valor: ' + str(self.value)


class Log(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE, null = True)
    event = models.CharField(max_length=200)
    log_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-log_date']

# class ActuatorAlert(models.Model):
#     value = models.ForeignKey(Value, on_delete=models.CASCADE)
#     def __str__(self):
#         return str(self.value) + ' Actuador: ' + str(self.value.reading.actuator)