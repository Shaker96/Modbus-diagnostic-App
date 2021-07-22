# default import
from django.shortcuts import render
# app and django rest imports
import json
import minimalmodbus as modbus
from django.db.models import Max
from django.db.models import Prefetch
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from actuator_api.custom_classes.customPageNumberPagination import CustomPageNumberPagination
from .serializers import *
from .models import Actuator, Register, Reading, Value, CustomUser, Log
from django.core import serializers

class CreateRegularUser(APIView):
    def post(self, request):
        if request.user.role > 1 :
            return Response(data={"response": "Usted no posee permisos para realizar esta operacion."}, status=status.HTTP_403_FORBIDDEN)
        try:
            new_user = CustomUser.objects.create(
                username= request.data['username'],
                password= make_password(request.data['password']),
                first_name= request.data['first_name'],
                last_name= request.data['last_name'],
                idn= request.data['idn'],
                role= 2
            )
            new_user.full_clean()
            return Response(data={"response": "Nuevo usuario registrado."}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(data=e.message_dict, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    def post(self, request):
        Rtoken = request.data["refresh"]
        token = RefreshToken(Rtoken)
        token.blacklist()
        return Response(data={ 'logout successful' }, status=status.HTTP_200_OK)

class ActuatorInfo(APIView):
    def get(self, request, actuator_id):
        actuator = Actuator.objects.get(id=actuator_id)
        serializer = ActuatorSerializer(actuator)

        return Response(data={ 'data': serializer.data}, status=status.HTTP_200_OK)

class Actuators(APIView):
    def get(self, request):
        register_list = [1, 2, 12, 24, 23] #bits importantes de los holding registers
        # prefetch_related('reading_set').annotate(latest_reading_date=Max('reading__reading_date')).prefetch_related('value_set')
        actuators = Actuator.objects.all()
        data = []
        for actuator in actuators:
            reading = actuator.reading_set.prefetch_related(Prefetch('value_set', queryset=Value.objects.filter(register__in=register_list))).last()
            serializer = ActuatorsWithMainValuesSerializer(reading)
            data.append(serializer.data)
        # print(actuators[0].actuatoralert_set.all())
        return Response(data={ 'data': data }, status=status.HTTP_200_OK)

class ActuatorMovement(APIView):
    def post(self, request):
        position = int(request.data['position'])
        mb_addr = int(request.data['address'])
        writer = modbus.Instrument('COM1', mb_addr, mode='rtu', close_port_after_each_call=False, debug=True)
        writer.serial.baudrate = 9600
        move_to = 768 if position == 0 else 256 if position == 100 else position
        try: 
            if (move_to > 0 and move_to < 100): 
                writer.write_registers(0, [6656, move_to])
            elif (move_to in [768, 256, 512]):
                writer.write_register(0, move_to, number_of_decimals=0, functioncode=6, signed=False)
            else:
                return Response(data={ 'result': 'Posición Invalida' }, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(data={ 'result': False }, status=status.HTTP_400_BAD_REQUEST)

        actuator = Actuator.objects.get(modbus_address=mb_addr)
        l = Log(actuator=actuator, event=3)
        l.save()

        return Response(data={ 'result': True }, status=status.HTTP_200_OK)

class Alerts(APIView):
    def get(self, request):
        paginator = CustomPageNumberPagination()
        values = Value.objects.filter(alert=True, alert_seen=False)
        
        page = paginator.paginate_queryset(values, request)
        
        serializer = AlertSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)
        # return Response(data=serializer.data, status=status.HTTP_200_OK)

class Readings(APIView):
    def post(self, request):
        paginator = CustomPageNumberPagination()
        queryset = Reading.objects.filter(
            actuator_id=request.data['actuator_id'], 
            date__range=[request.data['date_from'], request.data['date_to']]
        )
        serializer = ReadingWithValuesSerializer(queryset, many=True)

        return Response(data={'results': serializer.data}, status=status.HTTP_200_OK)
        # page = paginator.paginate_queryset(queryset, request)

        # serializer = ReadingWithValuesSerializer(page, many=True)

        # return paginator.get_paginated_response(serializer.data)


class Events(APIView): 
    def get(self, request):
        paginator = CustomPageNumberPagination()
        logs = Log.objects.all()

        page = paginator.paginate_queryset(logs, request)

        serializer = EventsSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)
        
    def post(self, request):

        Log.objects.create(
            user= CustomUser.objects.filter(id=request.user.id)[0],
            actuator= Actuator.objects.filter(id=request.data['actuator_id'])[0] if 'actuator_id' in request.data else None,
            event= request.data['type']
        )

        print(request.user.id)

        return Response(data={ 'hola' }, status=status.HTTP_200_OK)