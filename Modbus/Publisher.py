import pika

def send_data(msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=repr(msg))
    print(" [x] Sent 'Hello World!'")
    connection.close()


# def send_data(status_arr):
#     # Making a POST request
#     print(repr(status_arr))
#     data = {'data': repr(status_arr)}
#     data_json = json.dumps(data)
#     print(data_json)

#     r = requests.post('http://127.0.0.1:8000/', data=data_json)

#     # check status code for response recieved
#     # success code - 200
#     print(r)




#     # for i in range(len(actuator_arr)):
#     #     save.(temp_arr[i][0], id, id), temp_arr[i][3]