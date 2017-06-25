


	

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin1=4
pin2=17
pin3=18
pin4=27

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)
GPIO.setup(pin4,GPIO.OUT)


try:
	
	
		
	GPIO.output(pin1,1)
	time.sleep(0.5)
	GPIO.output(pin1,0)
	time.sleep(0.5)
	GPIO.output(pin2,1)
	time.sleep(0.5)
	GPIO.output(pin2,0)
	time.sleep(0.5)
	GPIO.output(pin3,1)
	time.sleep(0.5)
	GPIO.output(pin3,0)
	time.sleep(0.5)
	GPIO.output(pin4,1)
	time.sleep(0.5)
	GPIO.output(pin4,0)
	time.sleep(0.5)
	GPIO.output(pin4,1)
	time.sleep(0.5)
	GPIO.output(pin4,0)
	time.sleep(0.5)
	GPIO.output(pin3,1)
	time.sleep(0.5)
	GPIO.output(pin3,0)
	time.sleep(0.5)
	GPIO.output(pin2,1)
	time.sleep(0.5)
	GPIO.output(pin2,0)
	time.sleep(0.5)
	GPIO.output(pin1,1)
	time.sleep(0.5)
	GPIO.output(pin1,0)
	time.sleep(0.5)
		
		
		
		
finally:
			
		
	print("cleaning up")
	GPIO.cleanup()
	

