#!/usr/bin/python
## tpb_scraper.py

from robobrowser import RoboBrowser
import re

def scrapeDetails(details):
	regex = 'Uploaded (?P<date>([-:\d\s]+)), Size (?P<sizeNum>(\d+\.\d+)) (?P<sizeMeas>(\w+)), ULed by (?P<uploader>(\w+))'
	# regex = 'Uploaded (?P<date>([-:\d\s]+)),'
	ret = re.search(regex,details.replace(u'\xa0',u' '))
	return ret.groupdict() if ret else {} 
	


base = "http://thepiratebay.se/search/"

search = "the green mile".replace(' ','%20')
opts = "/0/7/0"

url = base+search+opts

browser = RoboBrowser()
browser.open(url)

rows = browser.find_all('tr')

for row in rows:
	# print row
	elem = row.find('font',{'class':'detDesc'})
	if elem:
		print elem.text.replace('\n','')
		print scrapeDetails(elem.text.replace('\n',''))

# browser.follow_link('generateLink')
# browser.follow_link('HERE')
