#!/usr/bin/python
# main.py

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2,subprocess,json

# --------------------------------------------------------------+
from collections import deque
import pyaudio,wave,audioop,os,urllib2,urllib,time,math


# Microphone stream config.
CHUNK = 1024  # CHUNKS of bytes to read each time from mic
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
THRESHOLD = 3200  # The threshold intensity that defines silence
                  # and noise signal (an int. lower than THRESHOLD is silence).

SILENCE_LIMIT = 0.5  # Silence limit in seconds. The max ammount of seconds where
                   # only silence is recorded. When this time passes the
                   # recording finishes and the file is delivered.

PREV_AUDIO = 0.1  # Previous audio (in seconds) to prepend. When noise
                  # is detected, how much of previously recorded audio is
                  # prepended. This helps to prevent chopping the beggining
                  # of the phrase.
# --------------------------------------------------------------+


url='http://www.vezulu.com/api/stt/'
# url = 'http://NR20120189:59752/api/stt'
# url = 'http://192.168.51.65:59752/api/stt/'

def audio_int(num_samples=50):
    """ Gets average audio intensity of your mic sound. You can use it to get
        average intensities while you're talking and/or silent. The average
        is the avg of the 20% largest intensities recorded.
    """

    print "Getting intensity values from mic."
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    values = [math.sqrt(abs(audioop.avg(stream.read(CHUNK), 4))) 
              for x in range(num_samples)] 
    values = sorted(values, reverse=True)
    r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
    print " Finished "
    print " Average audio intensity is ", r
    stream.close()
    p.terminate()
    return r

def listen_for_speech(threshold=THRESHOLD, num_phrases=-1):
    """
    Listens to Microphone and extracts phrases, a "phrase" being a sound 
    surrounded by silence (according to threshold). num_phrases controls
    how many phrases to process before finishing the listening process 
    (-1 for infinite). 
    """

    #Open stream
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print "* Listening mic. "
    audio2send = []
    cur_data = ''  # current chunk  of audio data
    rel = RATE/CHUNK
    slid_win = deque(maxlen=SILENCE_LIMIT * rel)
    #Prepend audio from 0.5 seconds before noise was detected
    prev_audio = deque(maxlen=PREV_AUDIO * rel) 
    started = False
    n = num_phrases
    response = []

    while (num_phrases == -1 or n > 0):
        try:
            cur_data = stream.read(CHUNK)
        except Exception, e:
            # overflow error (bug in pyaudio) happens somewhat frequently... 
            # no fix so far (most stack awnswers have to do with macports, changing chunk doesn't help)
            # print e
            continue
        
        slid_win.append(math.sqrt(abs(audioop.avg(cur_data, 4))))
        #print slid_win[-1]
        if(sum([x > THRESHOLD for x in slid_win]) > 0):
            if(not started):
                print "Starting record of phrase"
                started = True
            audio2send.append(cur_data)
        elif (started is True):
            print "Finished"
            print len(audio2send)
            # The limit was reached, finish capture and deliver.
            filename = save_speech(list(prev_audio) + audio2send, p)
            send(filename)

            # Remove temp file. Comment line to review.
            # os.remove(filename)

            # Reset all
            started = False
            slid_win = deque(maxlen=SILENCE_LIMIT * rel)
            prev_audio = deque(maxlen=0.5 * rel) 
            audio2send = []
            n -= 1
            print "Listening ..."
        else:
            prev_audio.append(cur_data)

    print "* Done recording"
    stream.close()
    p.terminate()

    return response

def save_speech(data, p):
    """ Saves mic data to temporary WAV file. Returns filename of saved 
        file """

    # filename = 'output_'+str(int(time.time()))
    filename = 'output'
    # writes data to WAV file
    data = ''.join(data)
    wf = wave.open(filename + '.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(RATE)  # TODO make this value a function parameter?
    wf.writeframes(data)
    wf.close()
    return filename + '.wav'

def send(filePath):

	# Register the streaming http handlers with urllib2
	register_openers()

	# Start the multipart/form-data encoding of the file "DSC0001.jpg"
	# "image1" is the name of the parameter, which is normally set
	# via the "name" parameter of the HTML <input> tag.

	# headers contains the necessary Content-Type and Content-Length
	# datagen is a generator object that yields the encoded parameters
	datagen, headers = multipart_encode({"wav1": open(filePath, "rb")})

	# Create the Request object
	request = urllib2.Request(url, datagen, headers)
	# request = urllib2.Request("http://192.168.51.92:57747/api/capturedImage", datagen, headers)
	# request.add_header('audioChannels',);
	
	# Actually do the request, and get the response
	try:
		res = urllib2.urlopen(request).read()
		data = json.loads(res)
		print data
		# subprocess.check_output(('bash','speak.sh','you said '+data['text']))
		# subprocess.check_output(('bash','speak.sh','you said'))
	except urllib2.URLError, e:
		print e


def testSend():
    output = subprocess.check_output(('bash','record.sh'))
    send('test.wav')

# listen_for_speech()  # listen to mic.

testSend()
# send('test.wav')  # translate audio file

# for i in xrange(0,10):
#     audio_int()  # To measure your mic levels