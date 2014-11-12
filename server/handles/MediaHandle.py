#!/usr/bin/python
## RemotesHandler.py

from Handle import Handle
from HandleResult import HandleResult
import re
import systemUtils as system
from temp.IMDBSource import IMDBSource

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class MediaHandle(Handle):

	def handle(self,request):	
		handled = False

		match = re.search('.*(is|was) (?P<actor>(\w+\s*)+) in( the (movie|show|tv show|series|tv series))? (?P<feature>(\w+\s*)+)', request)
		print request
		print match
		if match:
			print match.groupdict()
			# system.speak("I don't recall, let me check")
			vals = match.groupdict()
			source = IMDBSource()
			features = source.search_title(vals['feature'])
			# actor = source.search_actor(vals['actor'])[0]

			for feat in features:
				# source.db.update(feat)
				print feat['year']
				print feat['kind']
				if 'year' in feat: 
					print 'ya'
				if 'cover url' in feat:
					print feat['cover url']


			features = [feat['title'] for feat in features]

			print process.extract(vals['feature'],features,limit=len(features))

			return HandleResult(self,handled=True)

			# found = source.isIn_quick(vals['name'],feature)
			# print found
			# if found[1]>85:
			# 	system.speak(found[0]+' is in the '+str(feature['year'])+' '+feature['kind']+' '+feature['title']);
			# else:
			# 	system.speak(vals['name']+' is not in the '+str(feature['year'])+' '+feature['kind']+' '+feature['title'])

			# return HandleResult(self,handled=True,extras={'closest':found[0],'score':found[1]})



		if re.search('.*play.*last week tonight.*', request):
			system.playVideo('/home/pi/media/nancy/media/movies/tv/test.mp4')
			handled = True

		if re.search('.*stop.*video|playback.*', request):
			system.stopVideo()
			handled = True

		return HandleResult(self,handled=handled)