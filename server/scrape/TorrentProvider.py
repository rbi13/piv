#!/usr/bin/python
## systemUtils.py

# from handles.systemUtils import systemUtils as system
import tpb_scraper

## use this class to aggregate several sources:
# 	- look through all sources until 'sufficient' result found
# 	- implement a "fuzzy criteria profile" for an aggreate fuzzy score for result comparison
# 	- dynamically prioritize sources based on past performance

# replicate the handles provider interface for this desgin


class TorrentProvider:

	# temporary for poc, until provider pattern implemented
	def searchTorrent(search,criteria=None):
		torrents = tpb_scraper.getTorrents(search)

		for tor in torrents:
			print torrents


