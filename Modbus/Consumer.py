import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../actuator_project'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "actuator_project.settings")

import django
django.setup()
from django.conf import settings

from actuator_api.models import Reading, Actuator

import pika
import time

def receiveData(ch, method, properties, body):
    data = eval(body)
    key = data[0]
    data = data[1:]
    print(key)
    if(key == 'A'):
        for addr in data:
            a = Actuator(status=0, modbus_address=addr, model='ACT'+str(addr))
            a.save()

def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    channel.basic_consume(queue='hello', on_message_callback=receiveData, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    run()


# r = Reading.objects.count()
# print(r)
# r = Reading.objects.latest(reading_date)
# print(body)
# time.sleep(2)
# print(" listo " + body)