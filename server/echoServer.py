#!/usr/bin/python
## echoServer.py

from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import subprocess,unicodedata
 
class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '0.0.1',
                     'last_build':  date.today().isoformat() }
        self.write(response)
 
class echoHandler(tornado.web.RequestHandler):
    def get(self, phrase):

    	phrase = unicodedata.normalize('NFKD', phrase).encode('ascii','ignore')
    	speakPath = '/home/pi/dev/repos/picopi/picotts.sh'
    	output = subprocess.check_output(('bash',speakPath,phrase))

        response = { 'echo': phrase,
                     'requestTime': date.today().isoformat() }
        self.write(response)
 
application = tornado.web.Application([
    (r"/echo/(.*)", echoHandler),
    (r"/version", VersionHandler)
])
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()