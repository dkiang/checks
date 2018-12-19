from check50 import *


class cycle(Checks):

	@check()
	def exists(self):
		"""cycle.c exists."""
		self.require("cycle.c")

	@check("exists")
	def compiles(self):
		"""cycle.c compiles."""
		self.spawn("clang -std=c11 -o cycle cycle.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test1(self):
		"""identifies numbers less than 31"""
		self.spawn("./cycle 30 3 B").stdout("B C S S D E F A B S S C D E F A S S B C D E F S S A B C D E \n", "B C S S D E F A B S S C D E F A S S B C D E F S S A B C D E \n").exit(0)
	
	@check("compiles")
	def test2(self):
			"""identifies numbers greater than 31"""
			self.spawn("./cycle 33 3 B").exit(1)
	
	@check("compiles")
	def test3(self):
			"""identifies weeks starting with Saturday"""
			self.spawn("./cycle 28 1 A").stdout("S S A B C D E S S F A B C D S S E F A B C S S D E F A B \n", "S S A B C D E S S F A B C D S S E F A B C S S D E F A B \n").exit(0)

	@check("compiles")
	def test4(self):
			"""identifies weeks where Saturday is the 7th day"""
			self.spawn("./cycle 31 7 B").stdout("S B C D E F S S A B C D E S S F A B C D S S E F A B C S S D E \n", "S B C D E F S S A B C D E S S F A B C D S S E F A B C S S D E \n").exit(0)
	
	@check("compiles")
	def test5(self):
			"""identifies weeks where Saturday is the 6th day"""
			self.spawn("./cycle 31 6 B").stdout("B C D E F S S A B C D E S S F A B C D S S E F A B C S S D E F \n", "B C D E F S S A B C D E S S F A B C D S S E F A B C S S D E F \n").exit(0)