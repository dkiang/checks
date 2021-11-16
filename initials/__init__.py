import check50

from check50 import c

@check50.check()
def exists():
    """initials.c exists"""
    check50.exists("initials.c")

@check50.check(exists)
def compiles():
    """initials.c compiles"""
    check50.c.compile("initials.c", lcs50=True)

@check50.check(compiles)
def simple():
    """initials.c handles a simple first name"""
    check50.run("./initials").stdin("Bob").stdout("B\n").exit(0)

@check50.check(compiles)
def simple_double():
    """initials.c handles a simple name"""
    check50.run("./initials").stdin("Bobby Jones").stdout("BJ\n").exit(0)


@check50.check(compiles)
def complex():
    """initials.c handles a complex name"""
    check50.run("./initials").stdin("Bobby Jones Junior-Senior").stdout("BJJ\n").exit(0)

@check50.check(compiles)
def unrealistic():
    """initials.c handles a unrealistic name name"""
    check50.run("./initials").stdin("093284n 0983098 e0fdhsi haiyo23yu i8rd8sy 8y2 Io397984").stdout("00ehi8I\n").exit(0)
