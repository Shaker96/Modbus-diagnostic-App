import minimalmodbus as modbus
from Publisher import send_data
from DBActions import getActuators

def run():
    actuator_arr = getActuators()
    data = ['P']
    reader = modbus.Instrument('COM1', 0, mode='rtu', close_port_after_each_call=False, debug=True)
    for addr in actuator_arr:
        reader.address = addr
        flag = 0
        while flag < 10:
            try:
                res = reader.read_registers(4, 11)
                data += [addr] + res 
                send_data(data)
                flag = 10
            except:
                flag += 1
                print('error')
                if flag >= 10:
                    send_data([addr, False])

if __name__ == "__main__":
    run()