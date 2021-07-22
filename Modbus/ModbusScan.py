import minimalmodbus as modbus
from DBActions import storeActuators

def run():
    slaves = []
    addr = 1
    reader = modbus.Instrument('COM1', addr, mode='rtu', close_port_after_each_call=False, debug=False)
    reader.serial.baudrate = 9600
    while(addr <= 2): #2 debe ser reemplazado por 247, nro maximo de actuadores para red DDC
        reader.address = addr
        tries = 0
        while(tries < 3):
            try:
                r = reader.read_register(7, 0)
                tries = 3
                slaves.append(addr)
                print('act' + str(addr) + ' result ' + str(r))
            except:
                tries += 1
                print(str(addr) + ' empty, try ' + str(tries))
        addr += 1
    storeActuators(slaves)

if __name__ == "__main__":
    run()