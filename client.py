#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(3, GPIO.OUT)#motor 1,2 control
GPIO.setup(2, GPIO.OUT)#motor 1,2 control
GPIO.setup(4, GPIO.OUT)#motor 3,4 control
GPIO.setup(14, GPIO.OUT)#motor 3,4 control
GPIO.setup(11, GPIO.OUT)#support 1 control
GPIO.setup(12, GPIO.OUT)#support 1 control
GPIO.setup(13, GPIO.OUT)#support 2 control
GPIO.setup(15, GPIO.OUT)#support 2 control
GPIO.setup(23,GPIO.OUT)#enable
GPIO.setup(24,GPIO.OUT)#enable
GPIO.output(23, True)
GPIO.output(24, True)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7,True) #ping 1 sensor trigger
GPIO.setup(8, GPIO.IN)#ping 1 sensor ECHO
GPIO.setup(9, GPIO.OUT)
GPIO.output(9,True) #ping 1 sensor trigger
GPIO.setup(10, GPIO.IN)#ping 1 sensor ECHO
GPIO.setup(25,GPIO.OUT)#control hook
GPIO.setup(18,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)#enable
GPIO.output(15,True)
GPIO.setup(17,GPIO.OUT)#enable
GPIO.output(17,True)
GPIO.setup(27,GPIO.OUT)#control height hook
GPIO.setup(22,GPIO.OUT)

s = socket.socket()         # Create a socket object
host = '192.168.0.101' # Get local machine name
port = 8080               # Reserve a port for your service.

s.connect((host, port))
while True:

	p=s.recv(1024)
	print p
	if p=='l':
		GPIO.output(2, True)
		GPIO.output(3, False)
		GPIO.output(4, True)
		GPIO.output(14, False)
	if p=='r':
		GPIO.output(3, True)
                GPIO.output(2, False)
                GPIO.output(14, True)
                GPIO.output(4, False)
	if p=='hu':
                GPIO.output(25, True)
                GPIO.output(18, False)
		GPIO.output(22, False)
		GPIO.output(27,False)
        if p=='hd':
                GPIO.output(18, True)
                GPIO.output(25, False)
		GPIO.output(22, False)
                GPIO.output(27,False)
	if p=='lea':
                GPIO.output(27, True)
                GPIO.output(22, False)
		GPIO.output(18, False)
                GPIO.output(25,False)
	if p=='hold':
                GPIO.output(22, True)
                GPIO.output(27, False)
		GPIO.output(22, False)
                GPIO.output(25,False)	
	if p=='d':
		GPIO.output(2, True)
                GPIO.output(3, False)
                GPIO.output(14, True)
                GPIO.output(4, False)
	if p=='u':
		GPIO.output(3, True)
                GPIO.output(2, False)
                GPIO.output(4, True)
                GPIO.output(14, False)

	if p=='su':
		GPIO.output(11, True)
                GPIO.output(12, False)
                GPIO.output(13, True)
                GPIO.output(15, False)
	if p=='sd':
		GPIO.output(12, True)
                GPIO.output(11, False)
                GPIO.output(15, True)
                GPIO.output(13, False)
	if p=='stop':
                GPIO.output(2, False)
                GPIO.output(3, False)
                GPIO.output(14, False)
                GPIO.output(4, False)
	if p=='ping1':
		time.sleep(0.5)
		GPIO.output(7,True)
		time.sleep(0.00001)
		GPIO.output(7,False)
		start=time.time()
		while GPIO.input(8)==0:
			start=time.time()
		while GPIO.input(8)==1:
			stop=time.time()
		e=stop-start
		d=e*34000
		d=d/2
		print d
		if d>10:
			GPIO.output(2, False)
               		GPIO.output(3, False)
        	        GPIO.output(14, False)
	                GPIO.output(4, False)
	if p=='ping2':
                time.sleep(0.5)
                GPIO.output(9,True)
                time.sleep(0.00001)
                GPIO.output(9,False)
                start=time.time()
                while GPIO.input(10)==0:
                        start=time.time()
                while GPIO.input(10)==1:
                        stop=time.time()
                e=stop-start
                d=e*34000
                d=d/2
                print d
                if d>10:
                        GPIO.output(2, False)
                        GPIO.output(3, False)
                        GPIO.output(14, False)
                        GPIO.output(4, False)
		

GPIO.cleanup()
s.close                     # Close the socket when done
