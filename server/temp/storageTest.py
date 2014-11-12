#!/usr/bin/python
## storage.py

from pymongo import MongoClient

client = MongoClient()
# client = MongoClient('localhost', 27017)

db = client.test_db

name = 'Dave'

if not db.test_people.find_one({"name": name}):
	db.test_people.insert({'name': name})

for person in db.test_people.find():
	print person