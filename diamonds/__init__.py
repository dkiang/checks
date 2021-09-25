import re
import check50
import check50.c

@check50.check()
def exists():
    """diamond.c exists"""
    check50.exists("diamond.c")

@check50.check(exists)
def compiles():
    """diamond.c compiles."""
    check50.c.compile("diamond.c", lcs50=True)

@check50.check(compiles)
def prompts_user():
    """prompts user properly"""
    check50.run("./diamond").stdout("Size: ")

@check50.check(prompts_user)
def low_value():
    """rejects low value"""
    check50.run("./diamond").stdin("0").stdout("Size: ")

@check50.check(low_value)
def high_value():
    """rejects high value"""
    check50.run("./diamond").stdin("21").stdout("Size: ")

@check50.check(high_value)
def one():
    """1 row diamond"""
    print("*")
    print("\*")
    check50.run("./diamond").stdin("1").stdout("\*")

@check50.check(one)
def two():
    """2 row diamond"""
    check50.run("./diamond").stdin("2").stdout("\*\n\*")

@check50.check(two)
def three():
    """3 row diamond"""
    check50.run("./diamond").stdin("3").stdout(" \*\n\* \*\n \*")

@check50.check(three)
def four():
    """4 row diamond"""
    check50.run("./diamond").stdin("4").stdout(" \*\n\* \*\n\* \*\n \*")

@check50.check(four)
def five():
    """5 row diamond"""
    check50.run("./diamond").stdin("5").stdout("  \*\n \* \*\n\* \* \*\n \* \*\n  \*")

@check50.check(five)
def six():
    """6 row diamond"""
    check50.run("./diamond").stdin("6").stdout("  \*\n \* \*\n\* \* \*\n\* \* \*\n \* \*\n  \*")

@check50.check(six)
def seven():
    """7 row diamond"""
    check50.run("./diamond").stdin("7").stdout("   \*\n  \* \*\n \* \* \*\n\* \* \* \*\n \* \* \*\n  \* \*\n   \*")

@check50.check(seven)
def eight():
    """8 row diamond"""
    check50.run("./diamond").stdin("8").stdout("   \*\n  \* \*\n \* \* \*\n\* \* \* \*\n\* \* \* \*\n \* \* \*\n  \* \*\n   \*")

@check50.check(eight)
def nine():
    """9 row diamond"""
    check50.run("./diamond").stdin("9").stdout("    \*\n   \* \*\n  \* \* \*\n \* \* \* \*\n\* \* \* \* \*\n \* \* \* \*\n  \* \* \*\n   \* \*\n    \*")

@check50.check(nine)
def ten():
    """10 row diamond"""
    check50.run("./diamond").stdin("10").stdout("    \*\n   \* \*\n  \* \* \*\n \* \* \* \*\n\* \* \* \* \*\n\* \* \* \* \*\n \* \* \* \*\n  \* \* \*\n   \* \*\n    \*")

@check50.check(ten)
def eleven():
    """11 row diamond"""
    check50.run("./diamond").stdin("11").stdout("     \*\n    \* \*\n   \* \* \*\n  \* \* \* \*\n \* \* \* \* \*\n\* \* \* \* \* \*\n \* \* \* \* \*\n  \* \* \* \*\n   \* \* \*\n    \* \*\n     \*")

@check50.check(eleven)
def twelve():
    """12 row diamond"""
    check50.run("./diamond").stdin("12").stdout("     \*\n    \* \*\n   \* \* \*\n  \* \* \* \*\n \* \* \* \* \*\n\* \* \* \* \* \*\n\* \* \* \* \* \*\n \* \* \* \* \*\n  \* \* \* \*\n   \* \* \*\n    \* \*\n     \*")

@check50.check(twelve)
def thirteen():
    """13 row diamond"""
    check50.run("./diamond").stdin("13").stdout("      \*\n     \* \*\n    \* \* \*\n   \* \* \* \*\n  \* \* \* \* \*\n \* \* \* \* \* \*\n\* \* \* \* \* \* \*\n \* \* \* \* \* \*\n  \* \* \* \* \*\n   \* \* \* \*\n    \* \* \*\n     \* \*\n      \*")

@check50.check(thirteen)
def fourteen():
    """14 row diamond"""
    check50.run("./diamond").stdin("14").stdout("      \*\n     \* \*\n    \* \* \*\n   \* \* \* \*\n  \* \* \* \* \*\n \* \* \* \* \* \*\n\* \* \* \* \* \* \*\n\* \* \* \* \* \* \*\n \* \* \* \* \* \*\n  \* \* \* \* \*\n   \* \* \* \*\n    \* \* \*\n     \* \*\n      \*")

@check50.check(fourteen)
def fifteen():
    """15 row diamond"""
    check50.run("./diamond").stdin("15").stdout("       \*\n      \* \*\n     \* \* \*\n    \* \* \* \*\n   \* \* \* \* \*\n  \* \* \* \* \* \*\n \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \*\n  \* \* \* \* \* \*\n   \* \* \* \* \*\n    \* \* \* \*\n     \* \* \*\n      \* \*\n       \*")

@check50.check(fifteen)
def sixteen():
    """16 row diamond"""
    check50.run("./diamond").stdin("16").stdout("       \*\n      \* \*\n     \* \* \*\n    \* \* \* \*\n   \* \* \* \* \*\n  \* \* \* \* \* \*\n \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \*\n  \* \* \* \* \* \*\n   \* \* \* \* \*\n    \* \* \* \*\n     \* \* \*\n      \* \*\n       \*")

@check50.check(sixteen)
def seventeen():
    """17 row diamond"""
    check50.run("./diamond").stdin("17").stdout("        \*\n       \* \*\n      \* \* \*\n     \* \* \* \*\n    \* \* \* \* \*\n   \* \* \* \* \* \*\n  \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \*\n   \* \* \* \* \* \*\n    \* \* \* \* \*\n     \* \* \* \*\n      \* \* \*\n       \* \*\n        \*")

@check50.check(seventeen)
def eighteen():
    """18 row diamond"""
    check50.run("./diamond").stdin("18").stdout("        \*\n       \* \*\n      \* \* \*\n     \* \* \* \*\n    \* \* \* \* \*\n   \* \* \* \* \* \*\n  \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \*\n   \* \* \* \* \* \*\n    \* \* \* \* \*\n     \* \* \* \*\n      \* \* \*\n       \* \*\n        \*")

@check50.check(eighteen)
def nineteen():
    """19 row diamond"""
    check50.run("./diamond").stdin("19").stdout("         \*\n        \* \*\n       \* \* \*\n      \* \* \* \*\n     \* \* \* \* \*\n    \* \* \* \* \* \*\n   \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \* \*\n   \* \* \* \* \* \* \*\n    \* \* \* \* \* \*\n     \* \* \* \* \*\n      \* \* \* \*\n       \* \* \*\n        \* \*\n         \*")

@check50.check(nineteen)
def twenty():
    """20 row diamond"""
    check50.run("./diamond").stdin("20").stdout("         \*\n        \* \*\n       \* \* \*\n      \* \* \* \*\n     \* \* \* \* \*\n    \* \* \* \* \* \*\n   \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \* \*\n\* \* \* \* \* \* \* \* \* \*\n \* \* \* \* \* \* \* \* \*\n  \* \* \* \* \* \* \* \*\n   \* \* \* \* \* \* \*\n    \* \* \* \* \* \*\n     \* \* \* \* \*\n      \* \* \* \*\n       \* \* \*\n        \* \*\n         \*")
