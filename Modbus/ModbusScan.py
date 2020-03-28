import minimalmodbus as modbus
from Publisher import send_data

def run():
    slaves = ['A']
    addr = 1
    reader = modbus.Instrument('COM4', addr, mode='rtu', close_port_after_each_call=False, debug=False)
    while(addr <= 20):
        reader.address = addr
        tries = 0
        while(tries < 1):
            try:
                reader.read_register(7, 0)
                tries = 3
                slaves.append(addr)
                print('act' + str(addr))
            except:
                tries += 1
                print(str(addr) + ' empty, try ' + str(tries) )
        addr += 1
    send_data(slaves)

if __name__ == "__main__":
    run()