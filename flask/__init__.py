import check50
import check50.c

@check50.check()
def exists():
    """application.py exists."""
    check50.exists("application.py")
    """style.css exists."""
    check50.exists("static/style.css")
    """layout.html exists."""
    check50.exists("templates/layout.html")
    """index.html exists."""
    check50.exists("templates/index.html")
    """oops.html exists."""
    check50.exists("templates/oops.html")
    """cross.html exists."""
    check50.exists("templates/cross.html")