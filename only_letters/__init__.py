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
  def test1(self):
  """Checks lack of arguments"""
    self.spawn("./only_letters").exit(1)

@check50.check(compiles)
  def test2(self):
  """Checks too many arguments"""
    self.spawn("./only_letters hello world").exit(1)

@check50.check(compiles)
  def test3(self):
  """Checks for all letters"""
    self.spawn("./only_letters hello").stdout("Those are all letters.\n").exit(0)

@check50.check(compiles)
  def test4(self):
  """Checks for symbols"""
    self.spawn("./only_letters hel-lo").stdout("Those are not all letters.\n").exit(0)

@check50.check(compiles)
  def test5(self):
  """Checks for numbers"""
    self.spawn("./only_letters hello1").stdout("Those are not all letters.\n").exit(0)

@check50.check(compiles)
  def test6(self):
  """Checks for single letter"""
    self.spawn("./only_letters a").stdout("Those are all letters.\n").exit(0)