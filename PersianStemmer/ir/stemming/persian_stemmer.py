'''
	File name: persian_stemmer.py
	Author: Hossein Taghi-Zadeh
	Date created: 25/09/2016
	Date last modified: 25/12/2016
'''

__author__ = 'Hossein Taghi-Zadeh'
__email__ = "h.t.azeri@gmail.com"

from patricia import trie
import re
import unicodedata
import os
from .htz.ir.stemming.stemming_rule import StemmingRule
from .htz.ir.stemming.verb_stem import VerbStem
from .htz.utils import Utils

class PersianStemmer(object):
	lexicon = trie()
	mokassarDic = trie()
	cache = trie()
	verbDic = trie()
	_ruleList = []
	
	verbAffix = ["*ش", "*نده", "*ا", "*ار", "وا*", "اثر*", "فرو*", "پیش*", "گرو*","*ه","*گار","*ن"]
	suffix = ["كار", "ناك", "وار", "آسا", "آگین", "بار", "بان", "دان", "زار", "سار", "سان", "لاخ", "مند", "دار", "مرد", "کننده", "گرا", "نما", "متر"]
	prefix =  ["بی", "با", "پیش", "غیر", "فرو", "هم", "نا", "یک"]
	prefixException = ["غیر"]
	suffixZamir = ["م", "ت", "ش"]
	suffixException = ["ها", "تر", "ترین", "ام", "ات", "اش"]
	
	PATTERN_FILE_NAME = os.path.dirname(__file__) + "\\data\\Patterns.fa"
	VERB_FILE_NAME = os.path.dirname(__file__) + "\\data\\VerbList.fa"
	DIC_FILE_NAME = os.path.dirname(__file__) + "\\data\\Dictionary.fa"
	MOKASSAR_FILE_NAME = os.path.dirname(__file__) + "\\data\\Mokassar.fa"
	patternCount = 1
	enableCache = True
	enableVerb = False
	
	def __init__(self):
		try:
			self.loadRule()
			self.loadLexicon()
			self.loadMokassarDic()
			if self.enableVerb:
				self.loadVerbDic()
		except Exception as ex:
			print(ex)

	def loadData(self, resourceName):
		result = []
		with open(resourceName, 'r', encoding="utf-8") as reader:
			result = [line.strip("\r\n ") for line in reader if line.strip("\r\n ")]
		return result

	def loadVerbDic(self):
		if len(PersianStemmer.verbDic) > 0:
			return

		lines = self.loadData(PersianStemmer.VERB_FILE_NAME)
		for line in lines:
			arr = line.split("\t")
			PersianStemmer.verbDic[arr[0].strip()] = VerbStem(arr[1].strip(), arr[2].strip())

	def str2bool(self, v):
		return v.lower() in ("yes", "true", "t", "1")

	def loadRule(self):
		if len(PersianStemmer._ruleList) > 0:
			return

		lines = self.loadData(PersianStemmer.PATTERN_FILE_NAME)
		for line in lines:
			arr = line.split(",")
			PersianStemmer._ruleList.append(StemmingRule(arr[0], arr[1], arr[2], int(arr[3]), self.str2bool(arr[4])))
		#PersianStemmer._ruleList = [StemmingRule(arr[0], arr[1], arr[2], int(arr[3]), self.str2bool(arr[4])) for line in lines for arr in line.split(",")]

	def loadLexicon(self):
		if len(PersianStemmer.lexicon) > 0:
			return

		lines = self.loadData(PersianStemmer.DIC_FILE_NAME)
		for line in lines:
			PersianStemmer.lexicon[line.strip("\r\n ")] = True

	def loadMokassarDic(self):
		if len(PersianStemmer.mokassarDic) > 0:
			return

		lines = self.loadData(PersianStemmer.MOKASSAR_FILE_NAME)
		for line in lines:
			arr = line.split("\t")
			PersianStemmer.mokassarDic[arr[0].strip()] = arr[1].strip()

	def strip_accents(self, s):
		return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

	def normalization(self, s):
		newString = []
		for ch in s:
			if ch == 'ي':
				newString.append('ی')
			elif ch in ['ة', 'ۀ']:
				newString.append('ه')
			elif ch in ['‌', '‏']:
				newString.append(' ')
			elif ch == 'ك':
				newString.append('ک')
			elif ch == 'ؤ':
				newString.append('و')
			elif ch in ['إ', 'أ']:
				newString.append('ا')
			elif ch in ['\u064B', #FATHATAN
						'\u064C', #DAMMATAN
						'\u064D', #KASRATAN
						'\u064E', #FATHA
						'\u064F', #DAMMA
						'\u0650', #KASRA
						'\u0651', #SHADDA
						'\u0652']: #SUKUN
				pass
			else:
				newString.append(ch)

		return ''.join(newString)

	def validation(self, sWord):
		return (sWord in PersianStemmer.lexicon)

	def removeZamir(self, sInput, bState):
		sRule = "^(?P<stem>.+?)((?<=(ا|و))ی)?(ها)?(ی)?((ات)?( تان|تان| مان|مان| شان|شان)|ی|م|ت|ش|ء)$"
		if bState:
			sRule = "^(?P<stem>.+?)((?<=(ا|و))ی)?(ها)?(ی)?(ات|ی|م|ت|ش| تان|تان| مان|مان| شان|شان|ء)$"
			
		return self.extractStem(sInput, sRule)
		
	def getMokassarStem(self, sWord):

		if sWord in PersianStemmer.mokassarDic:
			return PersianStemmer.mokassarDic[sWord]
		else:
			sNewWord = self.removeZamir(sWord, True)
			if sNewWord in PersianStemmer.mokassarDic:
				return PersianStemmer.mokassarDic[sNewWord]
			else:
				sNewWord = self.removeZamir(sWord, False)
				if sNewWord in PersianStemmer.mokassarDic:
					return PersianStemmer.mokassarDic[sNewWord]
		return ""

	def verbValidation(self, sWord):
		if sWord.find(' ') > -1:
			return ""

		j = 0
		for affix in PersianStemmer.verbAffix:
			if (j == 0 and (sWord[-1] == 'ا' or sWord[-1] == 'و')):
				sTemp = affix.replace("*", sWord + "ی")
			else:
				sTemp = affix.replace("*", sWord)

			if self.normalizeValidation(sTemp, True):
				return affix
			j = j + 1
		return ""

	def getPrefix(self, sWord):
		result = [sPrefix for sPrefix in PersianStemmer.prefix if sWord.startswith(sPrefix)]
		if len(result) > 0:
			return result[0]
		return ""

	def getPrefixException(self, sWord):
		result = [sPrefix for sPrefix in PersianStemmer.prefixException if sWord.startswith(sPrefix)]
		if len(result) > 0:
			return result[0]
		return ""

	def getSuffix(self, sWord):
		result = [sSuffix for sSuffix in PersianStemmer.prefixException if sWord.endswith(sSuffix)]
		if len(result) > 0:
			return result[0]
		return ""

	def inRange(self, d, f, t):
		return d >= f and d <= t

	def normalizeValidation(self, sWord, bRemoveSpace):
		sWord = sWord.strip()
		l = len(sWord) - 2
		result = self.validation(sWord)

		if not result and sWord.find('ا') == 0:
			result = self.validation(sWord.replace("ا", "آ", 1))

		if (not result and self.inRange(sWord.find('ا'), 1, l)):
			result = self.validation(sWord.replace('ا', 'أ'))

		if (not result and self.inRange(sWord.find('ا'), 1, l)):
			result = self.validation(sWord.replace('ا', 'إ'))

		if (not result and self.inRange(sWord.find("ئو"), 1, l)):
			result = self.validation(sWord.replace("ئو", "ؤ"))

		if (not result and sWord.endswith("ء")):
			result = self.validation(sWord.replace("ء", ""))		

		if (not result and self.inRange(sWord.find("ئ"), 1, l)):
			result = self.validation(sWord.replace("ئ", "ی"))
			
		if (bRemoveSpace):
			if (not result and self.inRange(sWord.find(' '), 1, l)):
				result = self.validation(sWord.replace(" ", ""))

		#	# دیندار
		#	# دین دار
		if (not result):
			sSuffix = self.getSuffix(sWord)
			if (sSuffix):
				sTemp = sWord.replace(sSuffix, " " + sSuffix)
				if sSuffix == "مند":
					sTemp = sWord.replace(sSuffix, "ه " + sSuffix)
				result = self.validation(sTemp)

		if (not result):
			sPrefix = self.getPrefix(sWord)
			if sPrefix:
				if (sWord.startswith(sPrefix + " ")):
					result = self.validation(sWord.replace(sPrefix + " ", sPrefix))
				else:
					result = self.validation(sWord.replace(sPrefix, sPrefix + " "))			

		if (not result):
			sPrefix = self.getPrefixException(sWord)
			if (sPrefix):
				if (sWord.startswith(sPrefix + " ")):
					result = self.validation(sWord.replace(sPrefix + " ", "", 1))
				else:
					result = self.validation(sWord.replace(sPrefix, "", 1))

		return result

	def isMatch(self, sInput, sRule):
		match = re.compile(sRule).search(sInput)
		if match:
			return True
		return False

	def extractStem(self, sInput, sRule, sReplacement="\g<stem>"):
		return re.sub(sRule, sReplacement, sInput).strip()

	def getVerb(self, input):
		if input in PersianStemmer.verbDic:
			vs = PersianStemmer.verbDic[input]
			if self.validation(vs.getPresent()):
				return vs.getPresent()
			return vs.getPast()
		return ""

	def PatternMatching(self, input, stemList=[]):
		terminate = False
		s = ""
		sTemp = ""
		for rule in PersianStemmer._ruleList:
			if terminate:
				return terminate
			
			sReplace = rule.getSubstitution().split(";")
			pattern = rule.getBody()

			if not self.isMatch(input, pattern):
				continue
			
			k = 0
			for  t in sReplace:
				if k > 0:
					break

				s = self.extractStem(input, pattern, t)
				if len(s) < rule.getMinLength():
					continue

				if rule.getPoS() == 'K': # Kasre Ezafe
					if len(stemList) == 0:
						sTemp = self.getMokassarStem(s)
						if sTemp:
							stemList.append(sTemp)#, pattern + " [جمع مکسر]")
							k = k + 1
						elif self.normalizeValidation(s, True):
							stemList.append(s)#, pattern)
							k = k + 1
						else:
							pass
							#addToLog("", pattern + " ::" + s + "}")
				elif rule.getPoS() == 'V': # Verb
					sTemp = self.verbValidation(s)
					if len(sTemp) == 0:
						stemList.append(s)# pattern + " : [" + sTemp + "]"
						k = k + 1
					else:
						pass
						#addToLog("", pattern + " ::تمام وندها}")
				else:
					if self.normalizeValidation(s, True):
						stemList.append(s)
						if rule.getState():
							terminate = True
							k = k + 1
					else:
						pass
						#addToLog("", pattern + " ::" + s + "}")
		return terminate

	def run(self, input):
		input = self.normalization(input).strip()

		if not input:
			return ""

		#Integer or english 
		if Utils.isEnglish(input) or Utils.isNumber(input) or len(input) <= 2:
			return input

		if self.enableCache and input in self.cache:
			return self.cache[input]

		s = self.getMokassarStem(input)
		if self.normalizeValidation(input, False):
			#stemList.add(input/*, "[فرهنگ لغت]"*/)
			if self.enableCache:
				self.cache[input] = input
			return input
		elif s:
			#addToLog(s/*, "[جمع مکسر]"*/)
			#stemList.add(s)
			if self.enableCache:
				self.cache[input] = s
			return s
		
		stemList = []
		terminate = self.PatternMatching(input, stemList)
		
		if self.enableVerb:
			s = self.getVerb(input)
			if s:
				stemList = [s]

		if len(stemList) == 0:
			if self.normalizeValidation(input, True):
				#stemList.add(input, "[فرهنگ لغت]")
				if self.enableCache:
					self.cache[input] = input #stemList.get(0))
				return input#stemList.get(0)
			stemList.append(input)#, "")

		if terminate and len(stemList) > 1:
			return self.nounValidation(stemList)

		if self.patternCount != 0:
			stemList.sort(reverse=self.patternCount >= 0)
			stemList = stemList[abs(self.patternCount)-1:]

		if self.enableCache:
			self.cache[input] = stemList[0]

		return stemList[0]

	def nounValidation(self, stemList):
		stemList.sort()
		lastStem = stemList[-1]

		if lastStem.endswith("ان"):
			return lastStem
		else:
			firstStem = stemList[0]
			secondStem = stemList[1].replace(" ", "")

			for sSuffix in PersianStemmer.suffixZamir:
				if secondStem == firstStem + sSuffix:
					return firstStem

		return lastStem
'''
	public final int stem(char[] s, int len) /*throws Exception*/:
		
		StringBuilder input = new StringBuilder()
		for (int i=0 i< len i++):
			input.append(s[i])
		}		
		String sOut = this.run(input.toString())
		
		if (sOut.length() > s.length)
			s =  new char[sOut.length()]
		for (int i=0 i< sOut.length() i++):
			s[i] = sOut.charAt(i)
		}			
		/*try:
			for (int i=0 i< Math.min(sOut.length(), s.length) i++):
				s[i] = sOut.charAt(i)
			}	
		}
		catch (Exception e):
			throw new Exception("stem: "+sOut+" - input: "+ input.toString())
		}*/
		
		return sOut.length()		
		
	}	
'''