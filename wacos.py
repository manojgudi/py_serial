from __future__ import division # For operations with floating numbers
import matplotlib.pyplot as pl
import numpy as np
import time
import serial
import datetime
import os

ser = serial.Serial(
	port='/dev/ttyUSB0', # By default it is USB0
	baudrate=9600,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
        timeout=2
)
try:
    
    man=None
    data=[0]*11
    while(man==None):
        ser.open()
        inp=ser.inWaiting()
        ser.write('0')
        ser.write('1')
        for i in range(10):
            data[i]=(ser.readline())
            print "value",data[i]
            ser.flushInput()
            time.sleep(2)            
        man=ser.readline()
    ser.close()        
except :
    print "yo mama"
    ser.close()
