#!/bin/bash

tryNetworkTTS(){
	bash /home/pi/dev/repos/speech/tts/googletts.sh $INPUT
	if [ $? != 0 ]
	then
		# ./festivaltts.sh $INPUT
		bash /home/pi/dev/repos/speech/tts/picotts.sh $INPUT
	fi
}

localTTS(){
	# ./festivaltts.sh $INPUT
	bash /home/pi/dev/repos/speech/tts/picotts.sh $INPUT
}


INPUT=""
OFFLINE=""

if [ "$1" == "-pipe" ]
then
	INPUT=$(cat)
	if [ -n "$2" ]
	then
		OFFLINE="$2"
	fi 
else
	OFFLINE="$1"
	if [ "$1" != "-f" ]
	then
		INPUT=$*
	else
		INPUT=${*:2}
	fi
fi

if [ "$OFFLINE" == "-f" ]
then
	localTTS
else
	tryNetworkTTS
fi
