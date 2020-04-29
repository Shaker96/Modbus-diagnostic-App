# default import
from django.shortcuts import render
# app and django rest imports
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Actuator


class Login(APIView):
    def post(self, request):
        return 1

class Actuators(APIView):
    def get(self, request):
        actuators = Actuator.objects.all().prefetch_related('reading_set')
        print(actuators.values())
        return Response(data={"actuators":1}, status=status.HTTP_200_OK)