import check50
import check50.c

@check50.check()
def exists():
    """application.py exists."""
    check50.exists("application.py")
    """style.css exists."""
    check50.exists("static/style.css")