#!/usr/bin/python
## echoServer.py

import requests
from bs4 import BeautifulSoup

baseUrl = 'https://google.com/search?q='

query = 'why is the sun red'

url = baseUrl+query.replace(' ','+')

r = requests.get(url)

soup = BeautifulSoup(r.text)

print soup.find({'class','_Tgc'})

print r.text.find('_Tgc')