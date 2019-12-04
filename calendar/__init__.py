import check50
import check50.c

@check50.check()
def exists():
	"""calendar.c exists."""
	check50.exists("calendar.c")

@check50.check(exists)
def compiles():
	"""calendar.c compiles."""
	check50.c.compile("calendar.c", lcs50=True)

@check50.check("compiles")
def midweek_greater_28():
		"""identifies months starting midweek that are greater than 28 """
		check50.run("./calendar 1 29").stdout("      1  2  3  4  5\n", " 6  7  8  9 10 11 12\n", "13 14 15 16 17 18 19\n", "20 21 22 23 24 25 26\n", "27 28 29 30 31").exit(0)
	
#	@check("compiles")
#	def test2(self):
#			"""identifies months starting with a full week that are greater than 28 """
#			self.spawn("./calendar 33 3 B").exit(1)
#	
#	@check("compiles")
#	def test3(self):
#			"""identifies weeks starting with Saturday"""
#			self.spawn("./calendar 28 1 A").stdout("S S A B C D E S S F A B C D S S E F A B C S S D E F A B \n", "S S A B C D E S S F A B C D S S E F A B C S S D E F A B \n").exit(0)
#
#	@check("compiles")
#	def test4(self):
#			"""identifies weeks where Saturday is the 7th day"""
#			self.spawn("./calendar 31 7 B").stdout("S B C D E F S S A B C D E S S F A B C D S S E F A B C S S D E \n", "S B C D E F S S A B C D E S S F A B C D S S E F A B C S S D E \n").exit(0)
#	
#	@check("compiles")
#	def test5(self):
#			"""identifies weeks where Saturday is the 6th day"""
#			self.spawn("./calendar 31 6 B").stdout("B C D E F S S A B C D E S S F A B C D S S E F A B C S S D E F \n", "B C D E F S S A B C D E S S F A B C D S S E F A B C S S D E F \n").exit(0)