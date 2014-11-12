#!/usr/bin/python
## voiceServer.py

from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import unicodedata

from handles import systemUtils as system
from handles.HandleResult import HandleResult
from handles.DefaultHandlesProvider import DefaultHandlesProvider

handles = []

def commandHandle(str):
    
    result = None
    for handle in handles:
        result = handle.handle(str)
        if result.handled: break

    if not result.handled:
        system.speak("I don't understand")

    return result


class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '0.0.1',
                     'last_build':  date.today().isoformat() }
        self.write(response)
 
class echoHandler(tornado.web.RequestHandler):
    def get(self, command):

    	command = unicodedata.normalize('NFKD', command).encode('ascii','ignore')

        result = commandHandle(command)

        response = { 'command': command,
                     'handled': result.handled,
                     'extras': result.extras,
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