import check50
import check50.c

@check50.check()
def exists():
	"""hello.c exists."""
	check50.exists("hello.c")

	@check("exists")
	def compiles(self):
		"""hello.c compiles."""
		check50.c.compile("./hello", lcs50=True)

	@check("compiles")
	def test1():
		"""Checks output"""
		check50.c.run("./hello").stdin("Douglas").stdout("Hello Douglas\n", "Hello Douglas\n").exit(0)