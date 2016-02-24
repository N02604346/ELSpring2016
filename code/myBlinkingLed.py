#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)	

def Blink():
	while True
		for i in range(0,3)
			GPIO.output(17,True)
			time.sleep(.2)
			GPIO.output(17,False)
			time.sleep(.2)
		time.sleep(5)
		for i in range(0,4)
			GPIO.output(17,True)
			time.sleep(.2)
			GPIO.output(17,False)
			time.sleep(.2)
		time.sleep(5)
	GPIO.cleanup()
Blink()

  

