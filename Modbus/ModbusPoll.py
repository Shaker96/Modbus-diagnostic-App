import minimalmodbus as modbus
from Publisher import send_data
from DBActions import getActuators

def run():
    actuator_arr = getActuators() # obtener actuadores desde la BDD
    reader = modbus.Instrument('COM1', 0, mode='rtu', close_port_after_each_call=False, debug=True)
    reader.serial.baudrate = 9600
    for addr in actuator_arr:
        reader.address = addr
        flag = 0
        while flag < 10: # 10 intentos
            try:
                res = reader.read_registers(4, 11)
                send_data([addr] + res)
                flag = 10
            except:
                flag += 1
                print('error')
                if flag >= 10:
                    send_data([addr]) # consulta fallida. envia solo direccion modbus

if __name__ == "__main__": # correr cada 10 seg para consultar data
    run()