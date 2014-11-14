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

from scrape.TorrentProvider import TorrentProvider

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

	def stripAttribute(self,att,results):
		return [res[att] for res in results]

	def getFuzzyTupples(self,search,att,results):
		ret = []
		for res in results:
			ret.append( ( fuzz.ratio(search,res[att]) ,res) )

		return sorted(ret,reverse=True) 


	def findTorrent(title):
		pass

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

			print 'movies'
			tups = self.getFuzzyTupples(vals['feature'],'title',movies)
			for res in tups:
				print res[0]
				print res[1]['title']
				print res[1]['year']
				print

			print tups[0][1].summary()
			print 
			ia.update(tups[0][1])

			print tups[0][1].summary()

			tp = TorrentProvider()
			tp.searchTorrent(search)

			return HandleResult(self,handled=True)


		if re.search('.*play.*last week tonight.*', request):
			system.playVideo('/home/pi/media/nancy/media/movies/tv/test.mp4')
			handled = True

		if re.search('.*stop.*video|playback.*', request):
			system.stopVideo()
			handled = True

		return HandleResult(self,handled=handled)