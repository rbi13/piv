#!/usr/bin/python
## DefaultHandlesProvider.py

from HandlesProvider import HandlesProvider
from RemotesHandle import RemotesHandle
from MediaHandle import MediaHandle

class DefaultHandlesProvider(HandlesProvider):

	def handlesList(self):
		return [RemotesHandle(),MediaHandle()]
