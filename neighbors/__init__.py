import check50
import check50.c

@check50.check()
def compiles():
    """Does neighbors.c compile?"""
    check50.c.compile("neighbors.c")

@check50.check(compiles)
def zero():
    """(0,0) returns 8"""
    check50.run("./neighbors 0 0").stdout("The sum of all the neighbors to row 0 and column 0 is 8.\n").exit(0)

@check50.check(compiles)
def one():
    """(1,1) returns 27"""
    check50.run("./neighbors 1 1").stdout("The sum of all the neighbors to row 1 and column 1 is 27.\n").exit(0)

@check50.check(compiles)
def two():
    """(2,2) returns 45"""
    check50.run("./neighbors 2 2").stdout("The sum of all the neighbors to row 2 and column 2 is 45.\n").exit(0)

@check50.check(compiles)
def three():
    """(3,3) returns 63"""
    check50.run("./neighbors 3 3").stdout("The sum of all the neighbors to row 3 and column 3 is 63.\n").exit(0)

@check50.check(compiles)
def four():
    """(4,4) returns 32"""
    check50.run("./neighbors 4 4").stdout("The sum of all the neighbors to row 4 and column 4 is 32.\n").exit(0)