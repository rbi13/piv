# !/usr/bin/python
# testing.py 

import os,piezo,irRecord
import RPi.GPIO as GPIO

PIEZO_PIN = 18

def recordUpdate(status):
	print status
	if(status == irRecord.IRREC_CONTINUE):
		piezo.simplePulse(PIEZO_PIN,3)
	elif(status == irRecord.IRREC_SUCCESS):
		piezo.simplePulse(PIEZO_PIN,10)
	elif(status == irRecord.IRREC_TIMEOUT):
		piezo.simplePulse(PIEZO_PIN,5)

## script

try:
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PIEZO_PIN,GPIO.OUT)

	irRecord.remoteTemplate(callback=recordUpdate)

	GPIO.cleanup()

except (KeyboardInterrupt, SystemExit):
	# print("exiting, resetting pins")
	# try:
	# 	os.remove('tout.conf')
	# except Exception, e:
	# 	pass
	
	GPIO.cleanup()
	sys.exit(1)