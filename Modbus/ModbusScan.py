import minimalmodbus as modbus
from Publisher import send_data

def run():
    slaves = ['A']
    addr = 1
    reader = modbus.Instrument('COM1', addr, mode='rtu', close_port_after_each_call=False, debug=False)
    while(addr <= 250):
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
    send_data(slaves)

if __name__ == "__main__":
    run()