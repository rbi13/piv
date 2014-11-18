#!/usr/bin/python
## RemotesHandler.py

from Handle import Handle
from HandleResult import HandleResult
import re
import systemUtils as system
import parsingUtils as parse

class RemotesHandle(Handle):

	def handle(self,request):	
		handled = False
		if re.search('.*turn.*TV.*on|off.*', request):
			system.sendIRSignal('tv','KEY_POWER')
			handled = True

		match = re.search('.*TV.*source(\s)*(?P<presses>\d+)?.*', request)
		if match:
			vals = match.groupdict()
			presses = parse.get_int(vals['presses'],1)
			system.sendIRSignal('tv','KEY_VIDEO',presses,length=3)
			handled = True

		match = re.search('.*TV.*channel(\s)*(?P<chan>(\d+\s*-\s*\d+)|\d+).*', request)
		if match:
			vals = match.groupdict()
			channel = vals['chan'].replace(" ","") # clean
			# convenience... probably not general
			if len(channel)==4:
				channel = parse.insert(channel,'-',2)
			system.sendIRNumber('tv',channel,length=0.2,enter=True)
			handled = True



		return HandleResult(self,handled=handled)

