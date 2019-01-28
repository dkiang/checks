from check50 import *


class Bubble(Checks):

    @check()
    def exists(self):
        """bubble.c exists."""
        self.require("bubble.c")

    @check("exists")
    def compiles(self):
        """bubble.c compiles."""
        self.spawn("clang -std=c11 -o bubble bubble.c -lcs50 -lm").exit(0)

    @check("compiles")
    def sorts(self):
        """sorts {64, 34, 25, 12, 22, 11, 90}"""
        self.spawn("./bubble").stdout("11 12 22 25 34 64 90 \n").exit(0)
