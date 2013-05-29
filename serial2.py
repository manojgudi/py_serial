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
ser.open() # Opens Serial Port communication with above configurations
interval=int(input('Enter Integer value sampling time: ')) #put this instead of 120
b='s' # Loading 'b' any initial value
data=[None]*(interval)
while (b!='q'):
        for i in range(interval): # 120 seconds = 120 Values
                ser.flushInput() # Clears the input buffer
                data[i]=ser.readline()
                time.sleep(1) # delay of 1 second
# Converting unformatted data into an integral value
                temp=data[i]
                temp=float(temp[:temp.find('\n')])
                data[i]=temp    
                print 'serial value(temperature in C): ',data[i]
# Calliberation of received data
                data[i]=float((1)*data[i]) # since when Serial value is 0017 the surrounding temperature is around 30Celsius
# Plotting data values
                pl.xlabel('Time in Secs')
                pl.ylabel('Temperature')
                pl.title('Temperature Values plot')            
                pl.plot(data)# Refer book "A Primer on Scientific data"... pg187
        b=raw_input('enter q to quit : ')
        pl.hold()
print 'You have quit the program'
print 'Average of the graph :', np.average(data), 'Celsius'

# Storing the temperature values in to a text file
fop=open('/home/manoj/Desktop/values.txt','a') # Creates a file instance/object for handling file writing operation
fop.write('\n')
for i in range(len(data)):
        fop.write(str(data[i]))
        fop.write('\n')
fop.write('\nAverage of values is ')
fop.write(str(np.average(data)))
fop.write('\n')
fop.write('values recorded on :')
fop.write(str(datetime.datetime.today()))
fop.close() # Closes the instance of file handling
ser.close() # Closing the Serial Port Communication
