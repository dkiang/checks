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
		"""identifies numbers greater than 31"""
		self.spawn("./cycle 30 3 B").stdout("B C S S D E F A B S S C D E F A S S B C D E F S S A B C D E \n", "B C S S D E F A B S S C D E F A S S B C D E F S S A B C D E \n").exit(0)