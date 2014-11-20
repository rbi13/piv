#!/usr/bin/python
## guessit_test.py


from guessit import guess_file_info

filename = 'The Green Mile (1999) 720p BrRip x264 - 1.25GB - YIFY'
info = 'filename'
options = {}

guess = guess_file_info(filename+'.avi', info, options,type='movie')

print guess
