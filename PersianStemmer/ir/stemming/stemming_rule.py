'''
	File name: stemming_rule.py
	Author: Hossein Taghi-Zadeh
	Date created: 25/09/2016
	Date last modified: 25/12/2016
'''

__author__ = 'Hossein Taghi-Zadeh'
__email__ = "h.t.azeri@gmail.com"

import random
import time
from datetime import datetime
from patricia import trie
import json

class StemmingRule:
	
	def __init__(self, sBody, sSubstitution, sPoS, iMinLength=2, bState=False):
		self.body = sBody
		self.substitution = sSubstitution
		self.PoS = sPoS
		self.minLength = iMinLength
		self.state = bState

	def getBody(self):
		return self.body

	def getSubstitution(self):
		return self.substitution

	def getPoS(self):
		return self.PoS

	def getMinLength(self):
		return self.minLength

	def getState(self):
		return self.state
