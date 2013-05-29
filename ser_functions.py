from __future__ import division # For operations with floating numbers
import time
import serial

# Initialize Serial port, default {baud 9600, stop_bits 1 {1.5, 2}, byte_size 8{5..8}
def ser_init(baud, bytesize, parity, stopbits):
	'''Returns a Serial object instance'''
	# Automatic port detection
	ports=['USB2', 'USB1', 'USB0', 'S0']
	
	for val in ports:
		try:
			port='/dev/tty'+val
			print port
			ser = serial.Serial(port, baud,  bytesize, parity,  stopbits)
			print("serial found on" + val)
			break
		except:
			ser = -1
			print "Failed"
			pass
	
	return(ser) 

#ser_init(9600, 8, 'N', 1)

def ser_read(delay=1, count=1, baud=9600, bytesize=serial.EIGHTBITS, parity='N', stopbits=serial.STOPBITS_ONE):
	
	'''ser_read(delay, count, baud, bytesize, parity, stopbits) where delay represents time delay after which serial value will be fetched, minimum/default value is 1 second, count is maximum number of serial values to be fetched, by default it is 1, default {baud 9600, stop_bits 1 {1.5, 2}, byte_size 8{5..8}
	'''

	# Call ser_init()
	ser = ser_init(baud, bytesize, parity, stopbits)
	
	if (ser) == -1 : 
		print "Serial port couldn't be initialized"
	else:
		# Open the port
		ser.open()
		
		# Return array of Serial value
		data=[]

		for i in range(count):
			ser.flushInput()
			data.append(ser.readline())

			# Formatting Output
			temp = data[i]
			temp = float(temp[:temp.find('\n')])
			data[i] = temp

			time.sleep(delay)

		return data	

print(ser_read(.5,7))

'''
# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/ttyUSB1', # By default it is USB0
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
'''

