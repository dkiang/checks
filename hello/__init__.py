import check50
import check50.c

@check50.check()
def exists():
	"""hello.c exists."""
	check50.exists("hello.c")

	@check50.check("exists")
	def compiles(self):
		"""hello.c compiles."""
		check50.c.compile("./hello", lcs50=True)

	@check50.check("compiles")
	def test1():
		"""Checks output"""
		check50.c.run("./hello").stdin("Douglas").stdout("Hello Douglas\n", "Hello Douglas\n").exit(0)