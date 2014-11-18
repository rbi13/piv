#!/usr/bin/python
## RemotesHandler.py

from Handle import Handle
from HandleResult import HandleResult
import re
import systemUtils as system
from temp.IMDBSource import IMDBSource

import imdb
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class MediaHandle(Handle):

	def seperate(self,results):
		movies = []
		shows = []
		for res in results:
			if res['kind'] in 'movie':
				movies.append(res)
			elif res['kind'] in 'tv series':
				shows.append(res)

		return (movies, shows)

	def handle(self,request):	
		handled = False

		# match = re.search('.*(is|was) (?P<actor>(\w+\s*)+) in( the (movie|show|tv show|series|tv series))? (?P<feature>(\w+\s*)+)', request)
		match = re.search('.*(download|get me|find me|get|find) (?P<feature>(\w+\s*)+)',request)
		if match:

			vals = match.groupdict()
			print vals['feature']

			ia = imdb.IMDb()
			features = ia.search_movie(vals['feature'])
			# actor = ia.search_person('emma stone')[0]

			(movies, shows) = self.seperate(features)

			system.speak(' '.join(['I have',str(len(movies)),'movies and',str(len(shows)),'shows']))



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