import check50
import check50.c

@check50.check()
def exists():
  """only_letters.c exists."""
  check50.exists("only_letters.c")

@check50.check(exists)
def compiles():
  """only_letters.c compiles."""
  check50.c.compile("only_letters.c", lcs50=True)

@check50.check(compiles)
def test1():
  """Checks lack of arguments"""
  check50.run("./only_letters").exit(1)

@check50.check(compiles)
def test2():
  """Checks too many arguments"""
  check50.run("./only_letters hello world").exit(1)

@check50.check(compiles)
def test3():
  """Checks for all letters"""
  check50.run("./only_letters hello").stdout("Those are all letters.\n").exit(0)

@check50.check(compiles)
def test4():
  """Checks for symbols"""
  check50.run("./only_letters hel-lo").stdout("Those are not all letters.\n").exit(0)

@check50.check(compiles)
def test5():
  """Checks for numbers"""
  check50.run("./only_letters hello1").stdout("Those are not all letters.\n").exit(0)

@check50.check(compiles)
def test6():
  """Checks for single letter"""
  check50.run("./only_letters a").stdout("Those are all letters.\n").exit(0)