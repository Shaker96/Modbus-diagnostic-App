from django.db import models

# Create your models here.

class Register(models.Model):
    register_number = models.SmallIntegerField()
    description = models.CharField(max_length=200)
    bit_number = models.SmallIntegerField(null = True)

class Actuator(models.Model):
    status = models.CharField(max_length=200)
    modbus_address = models.SmallIntegerField()
    model = models.CharField(max_length=200)

class Reading(models.Model):
    actuator_id = models.ForeignKey(Actuator, on_delete=models.CASCADE)
    reading_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['reading_date']
    
class Value(models.Model):
    register_id = models.ForeignKey(Register, on_delete=models.CASCADE)
    reading_id = models.ForeignKey(Reading, on_delete=models.CASCADE)
    value = models.IntegerField()

class User(models.Model):
    SUPERADMIN = 0
    ADMIN = 1
    REGULAR = 2

    Role = (
        (SUPERADMIN, 'SuperAdmin'),
        (ADMIN, 'Admin'),
        (REGULAR, 'Regular'),
    )

    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    role = models.IntegerField(choices=Role, default=REGULAR)

class Log(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    actuator_id = models.ForeignKey(Actuator, on_delete=models.CASCADE, null = True)
    event = models.CharField(max_length=200)
    log_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['log_date']
    

