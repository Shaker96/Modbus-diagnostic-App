import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../actuator_project'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "actuator_project.settings")

import django
django.setup()
from django.conf import settings
from actuator_api.models import Reading, Actuator

def storeActuators(data):
    for addr in data:
        print('data' + str(addr))
        a = Actuator(status=0, modbus_address=addr, model='ACT'+str(addr))
        a.save()

def storeReading(data):
    return data

def getActuators():
    return Actuator.objects.values_list('modbus_address', flat=True)