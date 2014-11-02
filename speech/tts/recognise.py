#!/usr/bin/python
## irRecord.py

try:
	import pocketsphinx as ps
except Exception, e:
	import pocketsphinx as ps





wavFile = file('test.wav','rb')
# wavFile.seek(44)

speechRec = ps.Decoder()
speechRec.decode_raw(wavFile)
result = speechRec.get_hyp()

print result[0]
print result[0]