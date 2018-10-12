#!/usr/bin/ env python

import time
import serial

ser = serial.Serial(
	port='/dev/ttyACM0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )
counter=0

def readSerial():
    x = ser.readline()
    return x

if __name__ == "__main__":
    while 1:
        val = readSerial()
        print val

    
