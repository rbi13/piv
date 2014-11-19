#!/usr/bin/python
## storage.py

from pymongo import MongoClient

# collections
CHANNEL_ALIAS = 'channel_alias'

def getInstance(db_name = 'default_db'):
	client = MongoClient()
	# client = MongoClient('localhost', 27017)
	return client[db_name]

#--------------------------------------------+
# channel aliases
def addChannelAlias(device,alias,channel):
	db = getInstance()
	db[CHANNEL_ALIAS].save({'_id': device+'_'+alias,'device':device,'channel':channel})

	for alias in db[CHANNEL_ALIAS].find():
		print alias

def getChannel(device,alias):
	ret = getInstance()[CHANNEL_ALIAS].find_one({'_id':device+'_'+alias})
	print ret
	return ret['channel'] if ret else None

#--------------------------------------------+