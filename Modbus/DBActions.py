import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../actuator_project'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "actuator_project.settings")

import django
django.setup()
from django.conf import settings
from actuator_api.models import Reading, Actuator, Register

def storeActuators(data):
    for addr in data:
        print('data' + str(addr))
        a = Actuator(status=0, modbus_address=addr, name='ACT'+str(addr))
        a.save()

def storeReading(data):
    addr = data[0]
    data = data[1:]
    raw = repr(data)
    for register in list(Register.objects.all()):
        return register.description + str(register.id) + str(register.bit_number)
    # for r in range(11):
    #     reg = Register.objects.get(register_number=r+4)
    #     reg
        
    # return data

def getActuators():
    return Actuator.objects.values_list('modbus_address', flat=True)

if __name__ == '__main__':
    storeReading([1, 0, 45, 34, 3, 3, 435, 57, 867, 786, 678, 978])