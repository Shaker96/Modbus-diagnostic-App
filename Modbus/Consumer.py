import pika
from DBActions import *
# import time

def receiveData(ch, method, properties, body):
    data = eval(body)
    print(data)
    print(storeReading(data))

def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='queue')
    channel.basic_consume(queue='queue', on_message_callback=receiveData, auto_ack=True)

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