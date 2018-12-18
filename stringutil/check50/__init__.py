from check50 import *

class StringUtil(Checks):
	
	@check()
	def exists(self):
		"""StringUtil.java exists"""
		self.require("StringUtil.java")
		
	@check("exists")
	def compiles(self):
		"""StringUtil.java compiles"""
		self.spawn("javac StringUtil.java").exit(0)
		
	@check("compiles")
	def runtests(self):
		"""input of It's a fine day yields output of yad enif a s'tI"""
		self.spawn("java StringUtil").stdin("It's a fine day").stdout("yad enif a s'tI", "yad enif a s'tI").exit(0)
		
	@check("reverses")
	def checkPalindrome(self):
		"""input of It's a fine day yields output of yad enif a s'tI"""
		self.spawn("java StringUtil").stdin("It's a fine day").stdout("yad enif a s'tI", "yad enif a s'tI").exit(0)