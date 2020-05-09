# default import
from django.shortcuts import render
# app and django rest imports
import json
from django.db.models import Max
from django.db.models import Prefetch
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ReadingWithValuesSerializer
from .models import Actuator, Register, Reading, Value

register_list = [1, 2, 12, 14, 23]

class Login(APIView):
    def post(self, request):
        return 1

class Actuators(APIView):
    def get(self, request):
        # prefetch_related('reading_set').annotate(latest_reading_date=Max('reading__reading_date')).prefetch_related('value_set')
        actuators = Actuator.objects.all()
        data = []
        for actuator in actuators:
            reading = actuator.reading_set.prefetch_related(Prefetch('value_set', queryset=Value.objects.filter(register__in=register_list))).last()
            serializer = ReadingWithValuesSerializer(reading)
            data.append(serializer.data)
        # print(actuators[0].actuatoralert_set.all())
        return Response(data=data, status=status.HTTP_200_OK)

class alerts(APIView):
    def get(self, request):
        