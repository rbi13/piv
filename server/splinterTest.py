#!/usr/bin/python
## downloader.py

from splinter import Browser
from selenium import webdriver


driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)

def writeFile(name,str):
	f = open(name,'w')
	f.write(str) # python will convert \n to os.linesep
	f.close()


# browser = Browser()
# browser = Browser('zope.testbrowser')
browser = Browser('phantomjs')

tubeBase = "http://www.tubeoffline.com/download-1channel-videos.php"

sourceBase = "http://www.primewire.ag/"
sourceArgs = "tv-1386995-Game-of-Thrones/season-3-episode-7"


# analyse url to skip initial visit
browser.visit(tubeBase)
browser.fill('video', sourceBase+sourceArgs)
browser.find_by_value('GET video').click()

writeFile('htm',browser.html)


browser.find_by_id('generateLink').click()


writeFile('htm2',browser.html)

# stupid way to do this
# for x in xrange(0,1000):
# 	try:
# 		print x
# 		browser.find_by_id('generateLink').click()
# 	except Exception, e:
# 		# browser.find_link_by_text('-> HERE <-').first.click()
# 		browser.find_link_by_text('-> HERE <-').click()
# 		break
	

print 'clicked'
