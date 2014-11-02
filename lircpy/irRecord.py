#!/usr/bin/python
## irRecord.py

import pexpect,os

IRREC_CONTINUE = 0;
IRREC_SUCCESS = 1;
IRREC_TIMEOUT = 2;

def remoteTemplate(callback):

	child = pexpect.spawn ('irrecord -d /dev/lirc0 tout.conf')
	
	child.expect ('Press RETURN to continue.')
	child.sendline ('')
	child.expect ('Now start pressing buttons on your remote control.')
	print child.after # output this vocally
	child.sendline ('')

	expt = ['\.\.\.','Please enter the name for the next button',
	'gap not found, can\'t continue']

	while True:
		i = child.expect(expt)
		if i == 0: # continue
			callback(IRREC_CONTINUE)
		if i == 1: # profile created
			callback(IRREC_SUCCESS)
			break
		if i == 2: # timeout
			callback(IRREC_TIMEOUT)
			break

	child.kill(0)