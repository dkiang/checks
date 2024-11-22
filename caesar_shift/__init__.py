import check50
import check50.c

@check50.check()
def exists():
  """caesar_shift.c exists."""
  check50.exists("caesar_shift.c")

@check50.check(exists)
def compiles():
  """caesar_shift.c compiles."""
  check50.c.compile("caesar_shift.c", lcs50=True)

@check50.check(compiles)
def no_args():
  """Checks lack of arguments"""
  check50.run("./caesar_shift").exit(1)

@check50.check(compiles)
def extra_args():
  """Checks too many arguments"""
  check50.run("./caesar_shift Z A 1").exit(1)

@check50.check(compiles)
def wrap():
  """Checks for proper wrap"""
  check50.run("./caesar_shift Z 5").stdout("Shifted: E\n").exit(0)

@check50.check(compiles)
def no_shift():
  """Checks for no shift"""
  check50.run("./caesar_shift A 0").stdout("Shifted: A\n").exit(0)

@check50.check(compiles)
def greater_shift():
  """Checks for large value for key"""
  check50.run("./caesar_shift A 27").stdout("Shifted: B\n").exit(0)
  
@check50.check(compiles)
def even_greater_shift():
  """Checks for really large value for key"""
  check50.run("./caesar_shift N 65").stdout("Shifted: A\n").exit(0)