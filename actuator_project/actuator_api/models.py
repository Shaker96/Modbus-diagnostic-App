from django.db import models

# Create your models here.

class Register(models.Model):
    register_number = models.IntegerField()
    description = models.CharField(max_length=200)

class Actuator(models.Model):
    status = models.CharField(max_length=200)
    modbus_address = models.IntegerField()
    model = models.CharField(max_length=200)

class Reading(models.Model):
    actuator_id = models.ForeignKey(Actuator, on_delete=models.CASCADE)
    reading_date = models.DateTimeField(("date readed"), auto_now=True)

    class Meta:
        ordering = ['reading_date']
    
class Value(models.Model):
    register_id = models.ForeignKey(Register, on_delete=models.CASCADE)
    reading_id = models.ForeignKey(Reading, on_delete=models.CASCADE)
    value = models.IntegerField()

class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    role = models.IntegerField()

class Log(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    actuator_id = models.ForeignKey(Actuator, on_delete=models.CASCADE)
    event = models.IntegerField()
    log_date = models.DateTimeField('date loged', auto_now=True)

    class Meta:
        ordering = ['log_date']
    

