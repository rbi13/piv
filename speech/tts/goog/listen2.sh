#!/bin/bash

key='AIzaSyCqCe34I7FMs3HmIZUYwGAmYjvxh0ocoMg'
url='https://www.google.com/speech-api/v2/recognize?output=json&client=chromium&key='
# ops='&client=chromium&maxresults=6&pfilter=2'
ops='lang=en-us'

curl -X POST \
--data-binary /dev/shm/out.flac \
--header 'Content-Type: audio/x-flac; rate=44100;' \
"$url$key$ops"