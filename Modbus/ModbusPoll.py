import minimalmodbus as modbus
from .Publisher import send_data

def run(actuator_arr):
    temp_dic = {}
    output_arr = []
    reader = modbus.Instrument('COM1', actuator_arr[0], mode='rtu', close_port_after_each_call=False, debug=True)
    for i in range(len(actuator_arr)):
        reader.address = actuator_arr[i]
        flag = 0
        while flag < 10:
            try:
                res = reader.read_registers(4, 11)
                data = [actuator_arr[i]] + res 
                send_data(data)
                flag = 10
            except:
                flag += 1
                print('error')
                if flag >= 10:
                    send_data([actuator_arr[i], False])

if __name__ == "__main__":
    run()