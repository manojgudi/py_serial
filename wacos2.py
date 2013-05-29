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
        timeout=3
)
count=30

while(count!=0): 
    ser.open()
    ser.write('0')
    ser.write('1')
    try:
        temp=float(ser.readline())        
    except:
        temp='Missed'
    # here i log man variable into database directly
    print 'value is',temp, count
    ser.close()
    time.sleep(2) # Can We reduce this ?
    count=count-1
    ser.open()
    ser.write('2')
    ser.write('3')
    ser.close()
    time.sleep(3)
    
