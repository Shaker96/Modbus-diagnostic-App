from django.db import models

# Create your models here.

class Parameters(models.Model):
    description = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)

class Readings(models.Model):
    parameter_id = models.ForeignKey(Parameters, on_delete=models.CASCADE)
    actuator_id = models.ForeignKey(Actuators, on_delete=models.CASCADE)
    quantity = models.DecimalField()

class Actuators(models.Model):
    status = models.CharField(max_length=200)
    modbus_address = models.IntegerField()
    model = models.CharField(max_length=200)

class Users(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    role = models.IntegerField()

class Logs(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    actuator_id = models.ForeignKey(Actuators, on_delete=models.CASCADE)
    event = models.IntegerField()
    log_date = models.DateTimeField('date loged')
    

