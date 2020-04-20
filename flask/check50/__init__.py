from check50 import *


class flask(Checks):

	@check()
	def exists(self):
		"""application.py exists."""
		self.require("application.py")
		"""style.css exists."""
		self.require("static/style.css")
		"""layout.html exists."""
		self.require("templates/layout.html")
		"""index.html exists."""
		self.require("templates/index.html")
		"""oops.html exists."""
		self.require("templates/oops.html")
		"""cross.html exists."""
		self.require("templates/cross.html")