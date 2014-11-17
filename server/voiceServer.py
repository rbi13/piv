#!/usr/bin/python
## voiceServer.py

from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import unicodedata

from handles import systemUtils as system
from handles.DefaultHandlesProvider import DefaultHandlesProvider

handles = []

def commandHandle(str):
    handled = False
    for handle in handles:
        handled = (handle.handle(str) or handled) 

    if not handled:
        system.speak("I don't understand")

    return handled


class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '0.0.1',
                     'last_build':  date.today().isoformat() }
        self.write(response)
 
class echoHandler(tornado.web.RequestHandler):
    def get(self, command):

    	command = unicodedata.normalize('NFKD', command).encode('ascii','ignore')

        handled = commandHandle(command)

        response = { 'command': command,
                     'handled': handled,
                     'requestTime': date.today().isoformat() }
        self.write(response)
 
application = tornado.web.Application([
    (r"/echo/(.*)", echoHandler),
    (r"/version", VersionHandler)
])
 
if __name__ == "__main__":

    handles = DefaultHandlesProvider().handlesList()

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()