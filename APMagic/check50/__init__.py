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
		self.spawn("./APMagic 50 50 20 80 53").stdout("Magic Off: 50.6\n", "Magic Off: 50.6\n").exit(0)
	
	def test2(self):
			"""Checks improving scores"""
			self.spawn("./APMagic 20 50 50 80").stdout("Magic On: 65.0\n", "Magic On: 65.0\n").exit(0)
			
	def test3(self):
			"""Checks improving scores"""
			self.spawn("./APMagic 1 2 3 4 5 6 7 8").stdout("Magic On: 6.5\n", "Magic On: 6.5\n").exit(0)
			
	def test4(self):
				"""Checks non-improving scores"""
				self.spawn("./APMagic 1 2 3 4 5 6 8 7").stdout("Magic Off: 6.5\n", "Magic Off: 4.5\n").exit(0)
		