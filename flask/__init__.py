import check50
import check50.c

@check50.check()
def appexists():
    """application.py exists."""
    check50.exists("application.py")

@check50.check(appexists)
def styleexists(): 
    """style.css exists."""
    check50.exists("static/style.css")

@check50.check(styleexists)
def indexexists(): 
    """style.css exists."""
    check50.exists("templates/index.html")

@check50.check(indexexists)
def layoutexists(): 
    """style.css exists."""
    check50.exists("templates/layout.html")
	
@check50.check(layoutexists)
def oopsexists(): 
    """style.css exists."""
    check50.exists("templates/oops.html")

@check50.check(oopsexists)
def crossexists(): 
	"""style.css exists."""
	check50.exists("templates/cross.html")