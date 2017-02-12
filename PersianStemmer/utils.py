'''
	File name: utils.py
	Author: Hossein Taghi-Zadeh
	Date created: 25/09/2016
	Date last modified: 25/12/2016
'''

__author__ = 'Hossein Taghi-Zadeh'
__email__ = "h.t.azeri@gmail.com"


import re

class Utils:

    @staticmethod
    def isMatch(regex, str):
        match = re.compile(regex).search(str)
        if match:
            return True
        return False

    @staticmethod
    def isEnglish(input):
        return Utils.isMatch("[a-z,:/`;'\\?A-Z*+~!@#=\\[\\]{}\\$%^&*().0-9]+", input)

    @staticmethod
    def isNumber(input):
        return Utils.isMatch("[0-9,.]+", input)

    @staticmethod
    def wordCount(input):
        if not input.strip():
            return 0
        return len(input.strip().split("\\s+"))
