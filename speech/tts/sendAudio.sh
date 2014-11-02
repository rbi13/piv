#!/bin/bash

url='http://www.vezulu.com/api/stt/'
file='test.wav'

curl -k -X POST \
--data-binary $file \
--header 'Content-Type: audio/x-wav; rate=16000;' \
"$url"