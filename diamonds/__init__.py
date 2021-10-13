import check50

from check50 import c

@check50.check()
def download():
    """ Downloading Tests """
    check50.run("wget https://raw.githubusercontent.com/Alexandre2006/checks/master/diamonds/sample.c")

@check50.check()
def test():
    """Sample test"""
    c.compile("sample.c")
    c.compile("diamonds.c")
    output = check50.run("./diamonds").stdin(10).stdout()
    expected_output = check50.run("./sample").stdin(10).stdout()
    if output == expected_output:
        return True
    else:
        return False
