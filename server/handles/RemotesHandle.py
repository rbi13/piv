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
		if re.search('.*turn.*TV.*on|off.*', request,re.IGNORECASE):
			system.sendIRSignal('tv','KEY_POWER')
			handled = True

		# video source
		match = re.search('.*TV.*(source|video|input)(\s)*(?P<presses>\d+)?.*', request,re.IGNORECASE)
		if not handled and match:
			vals = match.groupdict()
			presses = parse.get_int(vals['presses'],1)
			system.sendIRSignal('tv','KEY_VIDEO',presses,length=3)
			handled = True

		# channel aliasing
		match = re.search('.*(store|save|set).*(TV)?.*channel(\s)*(?P<chan>(\d+\s*(-|dash)\s*\d+)|\d+) as (?P<alias>(\w+\s*)+)', request,re.IGNORECASE)
		if not handled and match:
			vals = match.groupdict()
			channel = vals['chan'].replace(" ","").replace('dash','-')
			storage.addChannelAlias('tv',vals['alias'],channel)
			system.speak('saving channel '+vals['chan']+" as "+vals['alias'])
			handled = True

		# mute
		match = re.search('.*(TV.*(mute|unmute)|(mute|unmute).*TV)', request,re.IGNORECASE)
		if not handled and match:
			system.sendIRSignal('tv','KEY_MUTE')
			handled = True

		# set channel/volume incrementally
		match = re.search('.*TV\s*(?P<function>(volume|channel))?.*(?P<direction>(up|down))\s*(?P<presses>(\d+))?', request,re.IGNORECASE)
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
		match = re.search('.*TV.*channel(\s)*(?P<chan>(\w+\s*)+|(\d+\s*(-|dash)\s*\d+)|\d+)', request,re.IGNORECASE)
		if not handled and match:
			vals = match.groupdict()

			# alias
			if not parse.is_number(vals['chan']):
				channel = storage.getChannel('tv',vals['chan'])
			# numeric
			else:
				channel = vals['chan'].replace(" ","").replace('dash','-') # clean

			# convenience... probably not general
			# if channel and len(channel)==4:
				# channel = parse.insert(channel,'-',2)
			
			if channel:
				print channel
				system.sendIRNumber('tv',channel,length=0.2,enter=(len(channel)<6))
			else:
				system.speak('no channel saved under '+vals['chan'])
			handled = True

		return HandleResult(self,handled=handled)

