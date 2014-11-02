#!/bin/bash

hardware="plughw:1,0"
duration="3"
file="test.wav"

arecord -D $hardware -f cd -t wav -d $duration -r 16000 $file
aplay $file