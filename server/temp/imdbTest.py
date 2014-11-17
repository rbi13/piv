#!/usr/bin/python
## imdbTest.py

import imdb,imdbMovie
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def isIn_quick(actorName,movie):
	ia.update(movie)
	actors = [actor['name'] for actor in movie['cast']]
	extract = process.extractOne(actorName,actors)
	print extract

def seach_Title(title):
	ia = imdb.IMDb()
	res = ia.search_movie(title)


# searchTerm = 'inglorious bastards'
searchTerm = 'the notebok'

titles = [movie['title'] for movie in res]

isIn_quick('rachel mcadams',res[0])

# extract = process.extract(searchTerm,titles,limit=len(titles))

# print '-----------------------'
# print extract
