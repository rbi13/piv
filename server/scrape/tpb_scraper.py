#!/usr/bin/python
## tpb_scraper.py

from robobrowser import RoboBrowser
import re

def scrapeTitle(title):
	ret = {}
	ret['title'] = title.text.strip()
	ret['page_link'] = 'http://thepiratebay.se'+title['href']
	return ret

def scrapeDetails(row):
	ret = {}
	# details
	details = row.find('font',{'class':'detDesc'}).text.replace('\n','')
	if details:
		regex = 'Uploaded (?P<date>([-:\d\s]+)), Size (?P<sizeNum>(\d+(.\d+)?)) (?P<sizeMeas>(\w+)), ULed by (?P<uploader>(.*))'
		ret = re.search(regex,details.replace(u'\xa0',u' ')).groupdict()

	# media type
	types = row.find_all('a',{'title':'More from this category'})
	print types
	if types:
		ret['media_type'] = types[0].text
		ret['type'] = types[1].text

	# magnet link
	ret['magnet_link'] = row.find('a',{'title':'Download this torrent using magnet'})['href']
	
	# torrent links
	torrent_tag = row.find('a',{'title':'Download this torrent'})
	if torrent_tag:
		ret['torrent_link'] = torrent_tag['href'] 
	
	# comment count
	commentsTag = row.find('img',{'src':'/static/img/icon_comment.gif'})
	if commentsTag:
		ret['comments'] = re.search('(?P<comments>(\d+))',commentsTag['title']).groupdict()['comments']
	
	return ret 


def getTorrents(search,limit=20):

	base = "http://thepiratebay.se/search/"
	opts = "/0/7/0"
	search = search.replace(' ','%20')
	
	url = base+search+opts

	browser = RoboBrowser()
	browser.open(url)

	rows = browser.find_all('tr')
	torrents = []
	for row in rows:
		title = row.find('a',{'class':'detLink'})
		if title:
			tor = {}
			tor.update( scrapeTitle(title) )
			tor.update( scrapeDetails(row) )
			torrents.append(tor)
			if len(torrents) >= limit:
				break

	return torrents


if __name__ == "__main__":
	torrents = getTorrents('neighbours')

	for tor in torrents:
		print tor
		print 

