#!/usr/bin/python

from check50 import *

class hello(Checks):

	@check()
	def exists(self):
		"""hello.c exists."""
		self.require("hello.c")

	@check("exists")
	def compiles(self):
		"""hello.c compiles."""
		self.spawn("clang -std=c11 -o hello hello.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test1(self):
		"""Checks output"""
		self.spawn("./hello").stdin("Douglas").stdout("^Hello Douglas\n", "Hello Douglas\n").exit(0)