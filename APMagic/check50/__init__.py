from check50 import *


class APMagic(Checks):

	@check()
	def exists(self):
		"""APMagic.c exists."""
		self.require("APMagic.c")

	@check("exists")
	def compiles(self):
		"""APMagic.c compiles."""
		self.spawn("clang -std=c11 -o APMagic APMagic.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test1(self):
		"""Checks non-improving scores"""
		self.spawn("./APMagic 50 50 20 80 5").stdin().stdout("Magic Off: 50.6\n", "Magic Off: 50.6\n").exit(0)