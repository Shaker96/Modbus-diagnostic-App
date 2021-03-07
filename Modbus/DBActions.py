import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../actuator_project'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "actuator_project.settings")

import django
django.setup()
from django.conf import settings
from actuator_api.models import Reading, Actuator, Register, Value

def storeActuators(data):
    for addr in data:
        print('data' + str(addr))
        a = Actuator(status=0, modbus_address=addr, name='ACT'+str(addr))
        a.save()

def storeReading(data):
    actuator = Actuator.objects.get(modbus_address=data[0])
    
    data = data[1:]
    raw = repr(data)
    last_r = Reading.objects.filter(actuator=actuator).last()
    if last_r is not None:
        if last_r.raw_data == str(raw):
            print('iguales')
            return 0
    
    registers = Register.objects.all() 
    
    r = Reading(
        actuator=actuator,
        raw_data=raw,
        response_ok=True
    )
    r.save()

    for i in range(11):
        reg = registers.filter(register_number = i + 5)
        if reg:
            if reg.filter(bit_number=None).exists():
                storeValue(
                    reg[0],
                    r,
                    data[i]
                )
            else:
                storeBits(
                    reg, 
                    r,
                    data[i]
                )
    # for r in range(11):
    #     reg = Register.objects.get(register_number=r+4)
    #     reg
        
    # return data

def storeBits(registers, reading, raw_value):
    bit_array = bin(raw_value)[2:]                        # transform to binary
    bit_array = ('0' * (16 - len(bit_array))) + bit_array # fill with 0 to get len 16
    bit_array = bit_array[::-1]                           # reverse array to start at bit 0

    for reg in registers:
        storeValue(
            register= reg,
            reading= reading,
            value= int(bit_array[reg.bit_number])
        )

def storeValue(register, reading, value):
    v = Value(
        register= register,
        reading= reading,
        value= value
    )
    if register.min_value != None:
        if value < register.min_value or value > register.max_value:
            v.alert = True
    v.save()

def getActuators():
    return Actuator.objects.values_list('modbus_address', flat=True)

if __name__ == '__main__':
    storeReading([1, 381, 0, 0, 30, 23411, 32816, 0, 1, 0, 25, 50])