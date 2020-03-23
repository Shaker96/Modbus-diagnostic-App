from actuator_project.actuator_api.models import Parameter, Reading, Actuator, User, Log
from rest_framework import serializers

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Register
        fields = ['register_number', 'description', 'bit_number']

class ActuatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actuator
        fields = ['status', 'modbus_address', 'model']

class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reading
        fields = ['reading_date', 'actuator_id']

class ValueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Value
        fields = ['register_id', 'reading_id', 'value']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'role']

class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ['user_id', 'actuator_id', 'event', 'log_date']
