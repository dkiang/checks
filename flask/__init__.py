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