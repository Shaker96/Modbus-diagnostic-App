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
        fields = ['actuator', 'date']

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

    def to_representation(self, data):
        data = super(ReadingWithValuesSerializer, self).to_representation(data)
        value_set = data.get('value_set')
        actuator = data.get('actuator')
        actuator_data = {
            "name": actuator.get('name'),
            "data": [
                { 
                    "name": "Dir. Modbus",
                    "value": actuator.get('modbus_address')
                },
                {
                    "name": "temperatura",
                    "value": str(value_set[4].get('value')) + ' ' + value_set[4].get('register').get('unit')
                },
                {
                    "name": "Alimentacion",
                    "value": str(value_set[0].get('value')) + ' ' + value_set[0].get('register').get('unit')
                },
                {
                    "name": "Apertura",
                    "value": str(value_set[1].get('value')) + value_set[1].get('register').get('unit')
                },
                {
                    "name": "Modo",
                    "value": "Stop" if value_set[2].get('value') == 1 else ("Remoto" if value_set[3].get('value') == 1 else "Local") 
                }
            ]
        }

        return actuator_data

# ----------------- Alert serializers ---------------------------

class AlertSerializer(serializers.ModelSerializer):
    description = serializers.CharField(source='register.description')
    actuator = serializers.CharField(source='reading.actuator.name')
    date = serializers.DateTimeField(source='reading.date')
    class Meta:
        model = Value
        fields = ['description', 'actuator', 'date', 'value']

    # def to_representation(self, value):
    #     return {
    #         "description": value.register.description,
    #         "date": value.reading.date,
    #         "actuator": value.reading.actuator.name
    #     }