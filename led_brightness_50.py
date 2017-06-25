import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
button1=16
button2=12
led_pin = 17
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
my_pwm_17=GPIO.PWM(led_pin,100)
dutychange=100
my_pwm_17.start(dutychange)


try:
	
	while True:
		0<dutychange<100 
		if GPIO.input(button1)==0:
			my_pwm_17.ChangeDutyCycle(dutychange)
			if dutychange<100:
				dutychange=dutychange+5
			time.sleep(0.15)
			dutychange<100
		if GPIO.input(button2)==0:
			my_pwm_17.ChangeDutyCycle(dutychange)
			if dutychange>0:
				dutychange=dutychange-5
			time.sleep(0.15)
			dutychange>1
finally:
	GPIO.cleanup()






