from check50 import *


class Bin_search(Checks):

    @check()
    def exists(self):
        """bin_search.c exists"""
        self.require("bin_search.c")

    @check("exists")
    def compiles(self):
        """bin_search.c compiles"""
        self.spawn("clang -std=c11 -o bin_search bin_search.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_handles_addition(self):
        """bin search finds 2"""
        self.spawn("./bin_search").stdin("2").stdout("Found\n").exit(0)

    @check("compiles")
    def test_handles_subtraction(self):
        """bin search finds 14"""
        self.spawn("./bin_search").stdin("14").stdout("Found\n").exit(0)

    @check("compiles")
    def test_handles_division(self):
        """bin search does not find 9"""
        self.spawn("./bin_search").stdin("9").stdout("Not found!\n").exit(0)

