#!/usr/bin/python
## voiceHandle.py

from abc import ABCMeta, abstractmethod

class Handle:
	__metaclass__ = ABCMeta

	@abstractmethod
	def handle(self,request) : pass
