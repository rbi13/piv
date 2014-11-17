#!/usr/bin/python
## echoServer.py

from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import subprocess,unicodedata,re,os,signal


# temp
video_process = ''

def commandHandle(str):

    # tv power
    match = re.search('.*turn.*TV.*on|off.*', str)
    if match:
        subprocess.check_output(('irsend','SEND_ONCE','tv','KEY_POWER'))
        return 'yes'

    match = re.search('.*TV.*source.*', str)
    if match:
        subprocess.check_output(('irsend','SEND_ONCE','tv','KEY_VIDEO'))
        return 'yes'


    global video_process
    print video_process
    # test play video
    match = re.search('.*play.*last week tonight.*', str)
    if match:
        path = '/home/pi/media/nancy/media/movies/tv/'
        title = 'test.mp4'
        # title = 'HBO\ -\ Last\ Week\ Tonight\ with\ John\ Oliver\ -\ 1x10\ Wealth\ Gap\ -\ \[2014-07-21\].mp4'
        video_process = subprocess.Popen(['omxplayer','-o','hdmi','-r',path+title],preexec_fn=os.setsid)
        print video_process
        return 'yes'

    # test play video
    match = re.search('.*stop.*video|playback.*', str)
    if match:
        # video_process.terminate()
        if video_process:
            os.killpg(video_process.pid, signal.SIGTERM)
            video_process = None;
        return 'sure boss'


    return "no comprenday boss"

def speakResponse(phrase):
    speakPath = '/home/pi/dev/repos/picopi/picotts.sh'
    subprocess.check_output(('bash',speakPath,phrase))


class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '0.0.1',
                     'last_build':  date.today().isoformat() }
        self.write(response)
 
class echoHandler(tornado.web.RequestHandler):
    def get(self, command):

    	command = unicodedata.normalize('NFKD', command).encode('ascii','ignore')
        speak = commandHandle(command)
        speakResponse(speak)

        response = { 'command': command,
                     'requestTime': date.today().isoformat() }
        self.write(response)
 
application = tornado.web.Application([
    (r"/echo/(.*)", echoHandler),
    (r"/version", VersionHandler)
])
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()