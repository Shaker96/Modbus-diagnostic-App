from actuator_project.actuator_api.models import Parameter, Reading, Actuator, User, Log
from rest_framework import serializers

class ParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parameter
        fields = ['description', 'unit']

class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reading
        fields = ['parameter_id', 'actuator_id', 'quantity']

class ActuatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actuator
        fields = ['status', 'modbus_address', 'model']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'role']

class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ['user_id', 'actuator_id', 'event', 'log_date']
