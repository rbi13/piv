#!/usr/bin/python
## RemotesHandler.py

from Handle import Handle
from HandleResult import HandleResult
import re
import systemUtils as system
import parsingUtils as parse
import storageUtils as storage

class RemotesHandle(Handle):

	def handle(self,request):	
		handled = False
		
		# power
		if re.search('.*turn.*TV.*on|off.*', request):
			system.sendIRSignal('tv','KEY_POWER')
			handled = True

		# video source
		match = re.search('.*TV.*source(\s)*(?P<presses>\d+)?.*', request)
		if not handled and match:
			vals = match.groupdict()
			presses = parse.get_int(vals['presses'],1)
			system.sendIRSignal('tv','KEY_VIDEO',presses,length=3)
			handled = True

		# channel aliasing
		match = re.search('.*(store|save|set).*(TV)?.*channel(\s)*(?P<chan>(\d+\s*-\s*\d+)|\d+) as (?P<alias>\w+)', request)
		if not handled and match:
			vals = match.groupdict()
			storage.addChannelAlias('tv',vals['alias'],vals['chan'])
			handled = True

		# set channel/volume incrementally
		match = re.search('.*TV\s*(?P<function>(volume|channel))?.*(?P<direction>(up|down))\s*(?P<presses>(\d+))?', request)
		if not handled and match:
			vals = match.groupdict()
			key_press = ''.join(
				['KEY_',
				parse.get_str(vals['function'],'volume'),
				vals['direction']]).upper()
			
			presses = parse.get_int(vals['presses'],1)
			system.sendIRSignal('tv',key_press,presses,length=0.1)
			handled = True

		# set channel numerically / by alias
		match = re.search('.*TV.*channel(\s)*(?P<chan>(\w+)|(\d+\s*-\s*\d+)|\d+)', request)
		if not handled and match:
			vals = match.groupdict()

			# numeric
			if parse.is_number(vals['chan']):
				channel = vals['chan'].replace(" ","") # clean
				# convenience... probably not general
				if len(channel)==4:
					channel = parse.insert(channel,'-',2)
			# alias
			else:
				channel = storage.getChannel('tv',vals['chan'])
			
			if channel:
				print channel
				# system.sendIRNumber('tv',channel,length=0.2,enter=True)
			else:
				system.speak('no channel saved under '+vals['chan'])
			handled = True

		return HandleResult(self,handled=handled)

