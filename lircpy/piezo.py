#!/usr/bin/python
# !/usr/bin/python/
 # Piezo.py 

import time,sys
import RPi.GPIO as GPIO

def sound(pin,length):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(length)
	GPIO.output(pin,GPIO.LOW)

def simplePulse(pin,count):
	for y in xrange(0,count):
		for x in xrange(0,40):
			sound(pin,0.0005)
		time.sleep(0.05)

