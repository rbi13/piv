#!/usr/bin/python
## RemotesHandler.py

from Handle import Handle
import re,systemUtils
import systemUtils as system

class MediaHandle(Handle):

	def handle(self,request):	
		handled = False

		match = re.search('.*is|was\s+(?P<first>\w+)\s+(?P<last>\w*)\s+in\s+(?P<feature>\w+)', request)
		print request
		print match
		if match:
			print match.groupdict()

		if re.search('.*play.*last week tonight.*', request):
			system.playVideo('/home/pi/media/nancy/media/movies/tv/test.mp4')
			handled = True

		if re.search('.*stop.*video|playback.*', request):
			system.stopVideo()
			handled = True

		return handled