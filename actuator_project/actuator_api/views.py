# default import
from django.shortcuts import render
# app and django rest imports
from django.contrib.auth.models import Parameters, Readings, Actuators, Users, Logs
from rest_framework import viewsets
from rest_framework import permissions
from actuator_project.actuator_api.serializers import ParametersSerializer, ReadingsSerializer, ActuatorsSerializer, UsersSerializer, LogsSerializer

# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]