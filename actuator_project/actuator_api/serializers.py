from django.contrib.auth.models import Parameters, Readings, Actuators, Users, Logs
from rest_framework import serializers

class ParametersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parameters
        fields = ['description', 'unit']

class ReadingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Readings
        fields = ['parameter_id', 'actuator_id', 'quantity']

class ActuatorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actuators
        fields = ['status', 'modbus_address', 'model']

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'pasword', 'name', 'role']

class LogsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Logs
        fields = ['user_id', 'actuator_id', 'event', 'log_date']
