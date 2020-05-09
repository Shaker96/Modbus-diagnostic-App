from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

#----------------- Default model serializers ----------------------------------------  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'username']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['register_number', 'description', 'bit_number', 'unit', 'min_value', 'max_value']

class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = ['status', 'modbus_address', 'model', 'name']

class ReadingSerializer(serializers.ModelSerializer):
    actuator = ActuatorSerializer()
    class Meta:
        model = Reading
        fields = ['actuator', 'date', 'value_set']

class ValueSerializer(serializers.ModelSerializer):
    register = RegisterSerializer()
    reading = ReadingSerializer()
    class Meta:
        model = Value
        fields = ['register', 'reading', 'value']

class LogSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    actuator = ActuatorSerializer()
    class Meta:
        model = Log
        fields = ['user', 'actuator', 'event', 'log_date']

# ----------------- special serializers -------------------------

class ValueSetSerializer(serializers.ModelSerializer):
    register = RegisterSerializer()
    class Meta:
        model = Value
        fields = ['register', 'reading', 'value']

class ReadingWithValuesSerializer(serializers.ModelSerializer):
    actuator = ActuatorSerializer()
    value_set = ValueSetSerializer(many=True)
    class Meta:
        model = Reading
        fields = ['actuator', 'date', 'value_set']
    


    # def to_representation(self, value):
    #     return {
    #         "actuator": ActuatorSerializer(value.actuator).data,
    #         "date": value.date,
    #         "values_set": ValueSerializer(value.value_set.all()).data
    #     }