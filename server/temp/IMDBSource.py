#!/usr/bin/python
## imdbTest.py

import imdb
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class IMDBSource:

	def __init__(self):
		self.db = imdb.IMDb()

	def isIn_quick(self,actorName,movie):
		self.db.update(movie)
		actors = [actor['name'] for actor in movie['cast']]
		return process.extractOne(actorName,actors)

	def search_title(self,title):
		return self.db.search_movie(title)

	def search_actor(self,name):
		return self.db.search_person(name)


if __name__ == "__main__":
	# searchTerm = 'inglorious bastards'
	searchTerm = 'the notebok'

	titles = [movie['title'] for movie in res]

	isIn_quick('rachel mcadams',res[0])

	# extract = process.extract(searchTerm,titles,limit=len(titles))

	# print '-----------------------'
	# print extract
