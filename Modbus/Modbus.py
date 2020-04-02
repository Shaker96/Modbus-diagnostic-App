import time

import serial
import minimalmodbus as modbus


if __name__ == "__main__":
    # test = modbus.Instrument('COM1', 25, mode='rtu', close_port_after_each_call=False, debug=True)
    # test.serial.baudrate = 19200
    # test.serial.timeout = 0.1
    # ser.write(b'011000000001020100A7C0')
    # print(bytes(ser.read(1000)))
    # l = []
    # c = 0
    # while True:
    #     time.sleep(1)
    #     var = test.read_register(8, 0, 3)
    #     l.append(var)
    #     c += 1
    #     if c == 5:
    #         break
    # var = test.read_register(4, 0, 3)
    # var = test.read_register(7, 0)
    # var = test.write_registers(0, [6656, 100])
    e = [2]
    if e:
        print('hola')
    # print(var)

    #print(var)
    # print(l)var = test.write_register(0, 768, number_of_decimals=0, functioncode=6, signed=False)
    #test._perform_command(3, '\x00\x07\x00\x01')
    #test.write_registers(0, [6656, 95])
    #time.sleep(2)
    #print(var)




