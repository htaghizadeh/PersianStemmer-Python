'''
	File name: verb_stem.py
	Author: Hossein Taghi-Zadeh
	Date created: 25/09/2016
	Date last modified: 25/12/2016
'''

__author__ = 'Hossein Taghi-Zadeh'
__email__ = "h.t.azeri@gmail.com"

class VerbStem:
	
	def __init__(self, sPast, sPresent):
		self.setPresent(sPresent)
		self.setPast(sPast)

	def getPresent(self):
		return self.present
		
	def setPresent(self, value):
		self.present = value
		
	def getPast(self):
		return self.past
		
	def setPast(self, value):
		self.past = value
