from __future__ import division # For operations with floating numbers
import time
import serial
import datetime
import os
import MySQLdb

ser = serial.Serial(
	port='/dev/ttyUSB0', # By default it is USB0
	baudrate=9600,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
        timeout=2
)
print " Serial Por intiailized..."
fop=open('/home/manoj/Desktop/wacos.txt','a')

try:
    while(1):
        conn = MySQLdb.connect (host = "db4free.net", user = "kushal", passwd = "msdhoni", db = "arpy")
        cursor = conn.cursor ()

        cursor.execute("SELECT u_switch FROM switch")
        var=(cursor.fetchone())
        print var
        temp=list(var)
        temp=temp[0]
        temp=int(str(temp))
        print temp, "current u_switch value", str(datetime.datetime.today())
        
        ######## File Writing Sequence #########
        fop=open('/home/manoj/Desktop/wacos.txt','a')
        fop.write('\n')
        fop.write(str(temp))
        fop.write(str(datetime.datetime.today()))
        fop.close()
        ######## end #########

        if (temp==1):
            cursor.execute('UPDATE switch SET a_switch=1 WHERE id=1')
            ser.open()
            man=ser.readline()
            if (man!=None):
                print 'Serial Port communication succesful...'
            ser.write('0')
            ser.write('1')
            ser.close()
            cursor.close()
            conn.close ()
            time.sleep(50)
        else :
            cursor.execute('UPDATE switch SET a_switch=0 WHERE id=1')
            cursor.close ()
            conn.close ()
            time.sleep(50)
    
except TypeError:
    print'database Python asynchronous'
    # I should jump to try block here which I dont know how to do
