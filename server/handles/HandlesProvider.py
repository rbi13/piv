#!/usr/bin/python
## HandlesProvider.py

from abc import ABCMeta, abstractmethod

class HandlesProvider:
	__metaclass__ = ABCMeta

	@abstractmethod
	def handlesList(self) : pass