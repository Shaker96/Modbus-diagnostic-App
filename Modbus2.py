import minimalmodbus as modbus
import requests
import json


def readings(actuator_arr):
    temp_arr = []
    output_arr = []
    for i in range(len(actuator_arr)):
        reader = modbus.Instrument('COM4', actuator_arr[i], mode='rtu', close_port_after_each_call=False, debug=True)
        # agregar do while
        flag = True
        while flag:
            try:
                res = reader.read_registers(5, 10)
                temp_arr.append(res)
                flag = False
            except:
                print("Error")


def send_data(status_arr):
    # Making a POST request
    print(repr(status_arr))
    data = {'data': repr(status_arr)}
    data_json = json.dumps(data)
    print(data_json)

    r = requests.post('http://127.0.0.1:8000/', data=data_json)

    # check status code for response recieved
    # success code - 200
    print(r)




    # for i in range(len(actuator_arr)):
    #     save.(temp_arr[i][0], id, id), temp_arr[i][3]

def separate(num_reg):
    return bin(10)[2:]

# def save()


if __name__ == "__main__":
    send_data([2, 2])
