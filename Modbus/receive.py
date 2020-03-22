import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def receive_data(ch, method, properties, body):
    time.sleep(5)
    print(" [x] Received %r" % eval(body))


channel.basic_consume(
    queue='hello', on_message_callback=receive_data, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()