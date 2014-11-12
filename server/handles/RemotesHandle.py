#!/usr/bin/python
## RemotesHandler.py

from Handle import Handle
from HandleResult import HandleResult
import re
import systemUtils as system

class RemotesHandle(Handle):

	def handle(self,request):	
		handled = False
		if re.search('.*turn.*TV.*on|off.*', request):
			system.sendIRSignal('tv','KEY_POWER')
			handled = True

		elif re.search('.*TV.*source.*', request):
			system.sendIRSignal('tv','KEY_VIDEO')
			handled = True

		return HandleResult(self,handled=handled)


