import re
import check50
import check50.c

@check50.check()
def exists():
    """diamonds.c exists"""
    check50.exists("diamonds.c")

@check50.check(exists)
def compiles():
    """diamonds.c compiles."""
    check50.c.compile("diamonds.c", lcs50=True)

@check50.check(compiles)
def prompts_user():
    """prompts user properly"""
    check50.run("./diamonds").stdout("Size: ")

@check50.check(prompts_user)
def low_value():
    """rejects low value"""
    check50.run("./diamonds").stdin("0").stdout("Size: ")

@check50.check(prompts_user)
def high_value():
    """rejects high value"""
    check50.run("./diamonds").stdin("21").stdout("Size: ")

@check50.check(prompts_user)
def one():
    """1 row diamond"""
    print("*")
    print("\*")
    check50.run("./diamonds").stdin("1").stdout("\*")

@check50.check(prompts_user)
def two():
    """2 row diamond"""
    check50.run("./diamonds").stdin("2").stdout("\*\n\*")

@check50.check(prompts_user)
def three():
    """3 row diamond"""
    check50.run("./diamonds").stdin("3").stdout(" \*\n\* \*\n \*")

@check50.check(prompts_user)
def four():
    """4 row diamond"""
    check50.run("./diamonds").stdin("4").stdout(" \*\n\* \*\n\* \*\n \*")

@check50.check(prompts_user)
def five():
    """5 row diamond"""
    check50.run("./diamonds").stdin("5").stdout("  \*\n \* \*\n\* \* \*\n \* \*\n  \*")

@check50.check(prompts_user)
def six():
    """6 row diamond"""
    check50.run("./diamonds").stdin("6").stdout("  \*\n \* \*\n\* \* \*\n\* \* \*\n \* \*\n  \*")

@check50.check(prompts_user)
def seven():
    """7 row diamond"""
    check50.run("./diamonds").stdin("7").stdout("   \*\n  \* \*\n \* \* \*\n\* \* \* \*\n \* \* \*\n  \* \*\n   \*")

@check50.check(prompts_user)
def eight():
    """8 row diamond"""
    check50.run("./diamonds").stdin("8").stdout("   \*\n  \* \*\n \* \* \*\n\* \* \* \*\n\* \* \* \*\n \* \* \*\n  \* \*\n   \*")

@check50.check(prompts_user)
def nine():
    """9 row diamond"""
    check50.run("./diamonds").stdin("9").stdout("    \*\n   \* \*\n  \* \* \*\n \* \* \* \*\n\* \* \* \* \*\n \* \* \* \*\n  \* \* \*\n   \* \*\n    \*")

@check50.check(prompts_user)
def ten():
    """10 row diamond"""
    check50.run("./diamonds").stdin("10").stdout("    \*\n   \* \*\n  \* \* \*\n \* \* \* \*\n\* \* \* \* \*\n\* \* \* \* \*\n \* \* \* \*\n  \* \* \*\n   \* \*\n    \*")

@check50.check(prompts_user)
def eleven():
    """11 row diamond"""
    check50.run("./diamonds").stdin("11").stdout("     \*\n    \* \*\n   \* \* \*\n  \* \* \* \*\n \* \* \* \* \*\n\* \* \* \* \* \*\n \* \* \* \* \*\n  \* \* \* \*\n   \* \* \*\n    \* \*\n     \*")

@check50.check(prompts_user)
def twelve():
    """12 row diamond"""
    check50.run("./diamonds").stdin("12").stdout("     \*\n    \* \*\n   \* \* \*\n  \* \* \* \*\n \* \* \* \* \*\n\* \* \* \* \* \*\n\* \* \* \* \* \*\n \* \* \* \* \*\n  \* \* \* \*\n   \* \* \*\n    \* \*\n     \*")

@check50.check(prompts_user)
def thirteen():
    """13 row diamond"""
    check50.run("./diamonds").stdin("13").stdout("      \*\n     \* \*\n    \* \* \*\n   \* \* \* \*\n  \* \* \* \* \*\n \* \* \* \* \* \*\n\* \* \* \* \* \* \*\n \* \* \* \* \* \*\n  \* \* \* \* \*\n   \* \* \* \*\n    \* \* \*\n     \* \*\n      \*")

@check50.check(prompts_user)
def fourteen():
    """14 row diamond"""
    check50.run("./diamonds").stdin("14").stdout("      \*\n     \* \*\n    \* \* \*\n   \* \* \* \*\n  \* \* \* \* \*\n \* \* \* \* \* \*\n\* \* \* \* \* \* \*\n\* \* \* \* \* \* \*\n \* \* \* \* \* \*\n  \* \* \* \* \*\n   \* \* \* \*\n    \* \* \*\n     \* \*\n      \*")

@check50.check(prompts_user)
def fifteen():
    """15 row diamond"""
    check50.run("./diamonds").stdin("15").stdout("       \*\n      \* \*\n     \* \* \*\n    \* \* \* \*\n   \* \* \* \* \*\n  \* \* \* \* \* \*\n \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \*\n  \* \* \* \* \* \*\n   \* \* \* \* \*\n    \* \* \* \*\n     \* \* \*\n      \* \*\n       \*")

@check50.check(prompts_user)
def sixteen():
    """16 row diamond"""
    check50.run("./diamonds").stdin("16").stdout("       \*\n      \* \*\n     \* \* \*\n    \* \* \* \*\n   \* \* \* \* \*\n  \* \* \* \* \* \*\n \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \*\n  \* \* \* \* \* \*\n   \* \* \* \* \*\n    \* \* \* \*\n     \* \* \*\n      \* \*\n       \*")

@check50.check(prompts_user)
def seventeen():
    """17 row diamond"""
    check50.run("./diamonds").stdin("17").stdout("        \*\n       \* \*\n      \* \* \*\n     \* \* \* \*\n    \* \* \* \* \*\n   \* \* \* \* \* \*\n  \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \*\n   \* \* \* \* \* \*\n    \* \* \* \* \*\n     \* \* \* \*\n      \* \* \*\n       \* \*\n        \*")

@check50.check(prompts_user)
def eighteen():
    """18 row diamond"""
    check50.run("./diamonds").stdin("18").stdout("        \*\n       \* \*\n      \* \* \*\n     \* \* \* \*\n    \* \* \* \* \*\n   \* \* \* \* \* \*\n  \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \*\n   \* \* \* \* \* \*\n    \* \* \* \* \*\n     \* \* \* \*\n      \* \* \*\n       \* \*\n        \*")

@check50.check(prompts_user)
def nineteen():
    """19 row diamond"""
    check50.run("./diamonds").stdin("19").stdout("         \*\n        \* \*\n       \* \* \*\n      \* \* \* \*\n     \* \* \* \* \*\n    \* \* \* \* \* \*\n   \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \* \*\n   \* \* \* \* \* \* \*\n    \* \* \* \* \* \*\n     \* \* \* \* \*\n      \* \* \* \*\n       \* \* \*\n        \* \*\n         \*")

@check50.check(prompts_user)
def twenty():
    """20 row diamond"""
    check50.run("./diamonds").stdin("20").stdout("         \*\n        \* \*\n       \* \* \*\n      \* \* \* \*\n     \* \* \* \* \*\n    \* \* \* \* \* \*\n   \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \* \*\n   \* \* \* \* \* \* \*\n    \* \* \* \* \* \*\n     \* \* \* \* \*\n      \* \* \* \*\n       \* \* \*\n        \* \*\n         \*")
