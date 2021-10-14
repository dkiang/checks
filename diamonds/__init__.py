import math

import check50

from check50 import c

simulated_output = ""


def print_row(size, spaces, extra_space):
    global simulated_output
    spaces = spaces - size
    i = 0
    while i < spaces:
        i += 1
        simulated_output += " "
    printed = 1
    if not extra_space:
        simulated_output += "*"
    else:
        simulated_output += " *"
    while printed < size:
        printed += 1
        simulated_output += " *"
    simulated_output += "\n"


def generate(rows, extra_space=False):
    global simulated_output
    simulated_output = ""
    if rows % 2 == 1:
        spacing = math.trunc(rows / 2) + 1
    else:
        spacing = math.trunc(rows / 2)
    length = math.trunc(rows / 2)
    current_length = 1
    while current_length <= length:
        print_row(current_length, spacing, extra_space)
        current_length += 1
    if rows % 2 == 1:
        print_row(spacing, spacing, extra_space)
    while current_length > 1:
        current_length -= 1
        print_row(current_length, spacing, extra_space)
    return simulated_output


def get_valid_outputs(rows):
    outputs = [generate(rows), generate(rows, True)]
    return outputs


def check(rows):
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && "
                           "./diamonds").stdin(str(rows)).stdout()
    if output in get_valid_outputs(rows):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(rows)[1], output)


@check50.check()
def compiles():
    """Does diamonds.c compile?"""
    check50.c.compile("diamonds.c", lcs50=True)


@check50.check(compiles)
def runs():
    """Does diamonds.c run?"""
    check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                  "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "10").exit()


@check50.check(runs)
def prompts():
    """Does diamonds.c prompt the user properly?"""
    check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                  "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdout(
        "Size: "
    )


@check50.check(runs)
def low_value():
    """Does diamonds.c reject a low value?"""
    check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                  "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "0").stdout("Size: ")


@check50.check(runs)
def high_value():
    """Does diamonds.c reject a high value?"""
    check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                  "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "21").stdout("Size: ")


@check50.check(runs)
def one():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 1 tall diamond?"""
    return check(1)
=======
    """1 row diamond"""
    check50.run("./diamonds").stdin("1").stdout("""*""")
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940


@check50.check(runs)
def two():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 2 tall diamond?"""
    return check(2)

=======
    """2 row diamond"""
    check50.run("./diamonds").stdin("2").stdout("*\n *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940

@check50.check(runs)
def three():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 3 tall diamond?"""
    return check(3)
=======
    """3 row diamond"""
    check50.run("./diamonds").stdin("3").stdout("""  *
 * *
  *""")
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940


@check50.check(runs)
def four():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 4 tall diamond?"""
    return check(4)

=======
    """4 row diamond"""
    check50.run("./diamonds").stdin("4").stdout("  *\n * *\n * *\n  *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940

@check50.check(runs)
def five():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 5 tall diamond?"""
    return check(5)

=======
    """5 row diamond"""
    check50.run("./diamonds").stdin("5").stdout("   *\n  * *\n * * *\n  * *\n   *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940

@check50.check(runs)
def six():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 6 tall diamond?"""
    return check(6)
=======
    """6 row diamond"""
    check50.run("./diamonds").stdin("6").stdout("   *\n  * *\n * * *\n * * *\n  * *\n   *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940


@check50.check(runs)
def seven():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 7 tall diamond?"""
    return check(7)

=======
    """7 row diamond"""
    check50.run("./diamonds").stdin("7").stdout("    *\n   * *\n  * * *\n * * * *\n  * * *\n   * *\n    *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940

@check50.check(runs)
def eight():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 8 tall diamond?"""
    return check(8)
=======
    """8 row diamond"""
    check50.run("./diamonds").stdin("8").stdout("    *\n   * *\n  * * *\n * * * *\n * * * *\n  * * *\n   * *\n    *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940


@check50.check(runs)
def nine():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 9 tall diamond?"""
    return check(9)

=======
    """9 row diamond"""
    check50.run("./diamonds").stdin("9").stdout("     *\n    * *\n   * * *\n  * * * *\n * * * * *\n  * * * *\n   * * *\n    * *\n     *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940

@check50.check(runs)
def ten():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 10 tall diamond?"""
    return check(10)
=======
    """10 row diamond"""
    check50.run("./diamonds").stdin("10").stdout("     *\n    * *\n   * * *\n  * * * *\n * * * * *\n * * * * *\n  * * * *\n   * * *\n    * *\n     *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940


@check50.check(runs)
def eleven():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 11 tall diamond?"""
    return check(11)

=======
    """11 row diamond"""
    check50.run("./diamonds").stdin("11").stdout("      *\n     * *\n    * * *\n   * * * *\n  * * * * *\n * * * * * *\n  * * * * *\n   * * * *\n    * * *\n     * *\n      *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940

@check50.check(runs)
def twelve():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 12 tall diamond?"""
    return check(12)

=======
    """12 row diamond"""
    check50.run("./diamonds").stdin("12").stdout("      *\n     * *\n    * * *\n   * * * *\n  * * * * *\n * * * * * *\n * * * * * *\n  * * * * *\n   * * * *\n    * * *\n     * *\n      *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940

@check50.check(runs)
def thirteen():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 13 tall diamond?"""
    return check(13)
=======
    """13 row diamond"""
    check50.run("./diamonds").stdin("13").stdout("       *\n      * *\n     * * *\n    * * * *\n   * * * * *\n  * * * * * *\n * * * * * * *\n  * * * * * *\n   * * * * *\n    * * * *\n     * * *\n      * *\n       *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940


@check50.check(runs)
def fourteen():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 14 tall diamond?"""
    return check(14)

=======
    """14 row diamond"""
    check50.run("./diamonds").stdin("14").stdout("       *\n      * *\n     * * *\n    * * * *\n   * * * * *\n  * * * * * *\n * * * * * * *\n * * * * * * *\n  * * * * * *\n   * * * * *\n    * * * *\n     * * *\n      * *\n       *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940

@check50.check(runs)
def fifteen():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 15 tall diamond?"""
    return check(15)
=======
    """15 row diamond"""
    check50.run("./diamonds").stdin("15").stdout("        *\n       * *\n      * * *\n     * * * *\n    * * * * *\n   * * * * * *\n  * * * * * * *\n * * * * * * * *\n  * * * * * * *\n   * * * * * *\n    * * * * *\n     * * * *\n      * * *\n       * *\n        *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940


@check50.check(runs)
def sixteen():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 16 tall diamond?"""
    return check(16)

=======
    """16 row diamond"""
    check50.run("./diamonds").stdin("16").stdout("        *\n       * *\n      * * *\n     * * * *\n    * * * * *\n   * * * * * *\n  * * * * * * *\n * * * * * * * *\n * * * * * * * *\n  * * * * * * *\n   * * * * * *\n    * * * * *\n     * * * *\n      * * *\n       * *\n        *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940

@check50.check(runs)
def seventeen():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 17 tall diamond?"""
    return check(17)
=======
    """17 row diamond"""
    check50.run("./diamonds").stdin("17").stdout("         *\n        * *\n       * * *\n      * * * *\n     * * * * *\n    * * * * * *\n   * * * * * * *\n  * * * * * * * *\n * * * * * * * * *\n  * * * * * * * *\n   * * * * * * *\n    * * * * * *\n     * * * * *\n      * * * *\n       * * *\n        * *\n         *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940


@check50.check(runs)
def eighteen():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 18 tall diamond?"""
    return check(18)

=======
    """18 row diamond"""
    check50.run("./diamonds").stdin("18").stdout("         *\n        * *\n       * * *\n      * * * *\n     * * * * *\n    * * * * * *\n   * * * * * * *\n  * * * * * * * *\n * * * * * * * * *\n * * * * * * * * *\n  * * * * * * * *\n   * * * * * * *\n    * * * * * *\n     * * * * *\n      * * * *\n       * * *\n        * *\n         *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940

@check50.check(runs)
def nineteen():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 19 tall diamond?"""
    return check(19)

=======
    """19 row diamond"""
    check50.run("./diamonds").stdin("19").stdout("          *\n         * *\n        * * *\n       * * * *\n      * * * * *\n     * * * * * *\n    * * * * * * *\n   * * * * * * * *\n  * * * * * * * * *\n * * * * * * * * * *\n  * * * * * * * * *\n   * * * * * * * *\n    * * * * * * *\n     * * * * * *\n      * * * * *\n       * * * *\n        * * *\n         * *\n          *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940

@check50.check(runs)
def twenty():
<<<<<<< HEAD
    """Does diamonds.c produce a proper 20 tall diamond?"""
    return check(20)
=======
    """20 row diamond"""
    check50.run("./diamonds").stdin("20").stdout("          *\n         * *\n        * * *\n       * * * *\n      * * * * *\n     * * * * * *\n    * * * * * * *\n   * * * * * * * *\n  * * * * * * * * *\n * * * * * * * * * *\n * * * * * * * * * *\n  * * * * * * * * *\n   * * * * * * * *\n    * * * * * * *\n     * * * * * *\n      * * * * *\n       * * * *\n        * * *\n         * *\n          *".rstrip())
>>>>>>> 8971019065e43c9c1962ac7ac4ec11bb54d3b940
