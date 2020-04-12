from actuator_project.actuator_api.models import Parameter, Reading, Actuator, Log
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
        fields = ['register', 'reading', 'value']

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'password', 'name', 'role']

class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ['user', 'actuator', 'event', 'log_date']
