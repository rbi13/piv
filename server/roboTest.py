#!/usr/bin/python
## downloader.py

from robobrowser import RoboBrowser


tubeBase = "http://www.tubeoffline.com/download-1channel-videos.php"

sourceBase = "http://www.primewire.ag/"
sourceArgs = "tv-1386995-Game-of-Thrones/season-3-episode-7"

browser = RoboBrowser()
browser.open(tubeBase)

form = browser.get_form(id='formStyle')
form['video'].value = sourceBase+sourceArgs
browser.submit_form(form)

link = browser.get_link(id='generateLink')

print browser.find(src="http://javaplugin.org/WL/grp1/gkpluginsAPI.js")

print browser.parsed

# browser.follow_link('generateLink')
# browser.follow_link('HERE')
