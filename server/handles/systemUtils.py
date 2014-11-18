#!/usr/bin/python
## systemUtils.py

import subprocess,re,os,signal
from time import sleep

video_process = None
speakPath = '/home/pi/dev/repos/picopi/picotts.sh'


# --------------------------------------------+
# Sound and speech

# uses picopi for offline speech synth
def speak(phrase): 
	subprocess.check_output(('bash',speakPath,phrase))

# (*rpi only)
def useHDMISound(useHDMI=True):
	out = '2' if useHDMI else '1'
	subprocess.check_output('amixer','-c','0','cset','numid=3',out)

# --------------------------------------------+
# Video playback and images

# uses omx player for command-line playback
def playVideo(path):
	global video_process
	if video_process:
		stopVideo()
	
	video_process = subprocess.Popen(['omxplayer','-o','hdmi','-r',path],preexec_fn=os.setsid)

def stopVideo():
	global video_process
	if video_process:
		os.killpg(video_process.pid, signal.SIGTERM)
		video_process = None;

def showImage(path):
	subprocess.check_output('fbi','-T','1','-noverbose',path)

def slideShow(paths,seconds):
	if seconds <= 0:
		subprocess.check_output('fbi','-T', '1','-noverbose'," ".join(paths))
	else:
		subprocess.check_output('fbi','-T','1','-t',str(seconds),'-noverbose', " ".join(paths))

# --------------------------------------------+
# remotes (IR, Network, etc...)
def sendIRSignal(device,key,repeat=1,length=0.8):
	
	subprocess.check_output(('irsend','SEND_ONCE',device,key))
	for x in xrange(1,repeat):
		sleep(length)
		subprocess.check_output(('irsend','SEND_ONCE',device,key))

def sendIRCombo(device,keys,length=0.2,enter=False):
	
	for key in keys:
		sleep(length) # not the best order here
		subprocess.check_output(('irsend','SEND_ONCE',device,key))
	if enter:
		subprocess.check_output(('irsend','SEND_ONCE',device,'KEY_ENTER'))

def sendIRNumber(device,num,length=0.2,enter=False):
	numStr = str(num)
	digits = ['KEY_BREAK' if ('-' == digit) else 'KEY_'+digit for digit in numStr]
	print digits
	sendIRCombo(device,digits,length,enter)

# --------------------------------------------+
