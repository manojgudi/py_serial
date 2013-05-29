from __future__ import division # For operations with floating numbers
import matplotlib.pyplot as pl
import numpy as np
import time
import serial
import datetime
import os
import pylab


pylab.ion()
# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/ttyUSB0', # By default it is USB0
	baudrate=9600,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)
ser.open()
ser.flushInput()
while (data!='nonsense'):
    data
ser.close()
