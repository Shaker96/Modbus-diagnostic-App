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
        fields = ['id', 'status', 'modbus_address', 'model', 'name']

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

class ActuatorsWithMainValuesSerializer(serializers.ModelSerializer):
    actuator = ActuatorSerializer()
    value_set = ValueSetSerializer(many=True)
    class Meta:
        model = Reading
        fields = ['actuator', 'date', 'value_set']

    def to_representation(self, data):
        data = super(ActuatorsWithMainValuesSerializer, self).to_representation(data)
        value_set = data.get('value_set')
        actuator = data.get('actuator')
        actuator_data = {
            "id": actuator.get('id'),
            "name": actuator.get('name'),
            "model": actuator.get('model'),
            "data": [
                { 
                    "name": "Dir. Modbus",
                    "value": actuator.get('modbus_address')
                },
                {
                    "name": "Temperatura",
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

class DiagnosisSerializer(serializers.ModelSerializer):
    value_set = ValueSetSerializer(many=True)
    class Meta:
        model = Reading
        fields = ['date', 'value_set', 'diagnosis_ok']

    def to_representation(self, data):
        data = super(DiagnosisSerializer, self).to_representation(data)
        value_set = data.get('value_set')
        date = data.get('date')
        diagnosis_ok = data.get('diagnosis_ok')
        actuator_data = {
            "date": date,
            "diagnosis_ok": diagnosis_ok,
            "data": [
                {
                    "name": "Alimentacion (" + value_set[0].get('register').get('unit') + ')',
                    "value": value_set[0].get('value')
                },
                {
                    "name": "Temperatura (" + value_set[1].get('register').get('unit') + ')',
                    "value": value_set[1].get('value')
                },
                {
                    "name": "Torque (" + value_set[2].get('register').get('unit') + ')',
                    "value": value_set[2].get('value')
                }
            ]
        }
        return actuator_data

class ReadingWithValuesSerializer(serializers.ModelSerializer):
    # actuator = ActuatorSerializer()
    value_set = ValueSetSerializer(many=True)
    class Meta:
        model = Reading
        fields = ['date', 'value_set']


class EventsSerializer(serializers.ModelSerializer):
    LOGIN = 0
    LOGOUT = 1
    SIGNUP = 2
    ACTUATOR = 3
    READING = 4
    READINGS = 5

    EVENTS = (
        ('El usuario ha iniciado sesión', 0),
        ('El usuario ha cerrado sesión', 1),
        ('Se ha creado un nuevo usuario', 2),
        ('Un actuador ha sido operado manualmente', 3),
        ('Nueva lectura disponible', 4),
        ('El usuario accedió a las lecturas del actuador', 5)
    )

    actuator = serializers.CharField(source='actuator.name', required=False)
    user = serializers.CharField(source='user.username', required=False)
    log_date = serializers.DateTimeField()
    event = serializers.CharField(source='get_event_display')
    class Meta: 
        model = Log
        fields = ['actuator', 'user', 'event', 'log_date']

    

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