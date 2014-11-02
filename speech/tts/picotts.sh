#!/bin/bash



bash /home/pi/temp/picopi/pico/tts/testtts "$1" | aplay --rate=16000 --channels=1 --format=S16_LE