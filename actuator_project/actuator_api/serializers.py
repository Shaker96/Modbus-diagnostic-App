from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Register
        fields = ['register_number', 'description', 'bit_number']

class ActuatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actuator
        fields = ['status', 'modbus_address', 'model', 'name']

class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reading
        fields = [ 'actuator', 'reading_date', 'raw_data', 'response_ok']

class ValueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Value
        fields = ['register', 'reading', 'value']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'username']

class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ['user', 'actuator', 'event', 'log_date']
