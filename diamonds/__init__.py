import math

import check50

from check50 import c

simulated_output = ""


def print_row(size, spaces, extra_space, extra_end_space=False):
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
    if extra_end_space:
        simulated_output += " "
    simulated_output += "\n"


def generate(rows, extra_space=False, extra_end_space=False):
    global simulated_output
    simulated_output = ""
    if rows % 2 == 1:
        spacing = math.trunc(rows / 2) + 1
    else:
        spacing = math.trunc(rows / 2)
    length = math.trunc(rows / 2)
    current_length = 1
    while current_length <= length:
        print_row(current_length, spacing, extra_space, extra_end_space)
        current_length += 1
    if rows % 2 == 1:
        print_row(spacing, spacing, extra_space, extra_end_space)
    while current_length > 1:
        current_length -= 1
        print_row(current_length, spacing, extra_space, extra_end_space)
    return simulated_output


def get_valid_outputs(rows):
    outputs = [generate(rows, False, False),
               generate(rows, True, False),
               generate(rows, False, True),
               generate(rows, True, True)]
    return outputs


def check(rows):
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && "
                           "./diamonds").stdin(str(rows)).stdout()
    if output in get_valid_outputs(rows):
        return True
    else:
        error = get_valid_outputs(rows)[0] + \
                "or\n" + get_valid_outputs(rows)[1] + \
                "or\n" + get_valid_outputs(rows)[2] +\
                "or\n" + get_valid_outputs(rows)[3]
        raise check50.Mismatch(error, output)


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
    """Does diamonds.c produce a proper 1 tall diamond?"""
    return check(1)


@check50.check(runs)
def two():
    """Does diamonds.c produce a proper 2 tall diamond?"""
    return check(2)


@check50.check(runs)
def three():
    """Does diamonds.c produce a proper 3 tall diamond?"""
    return check(3)


@check50.check(runs)
def four():
    """Does diamonds.c produce a proper 4 tall diamond?"""
    return check(4)


@check50.check(runs)
def five():
    """Does diamonds.c produce a proper 5 tall diamond?"""
    return check(5)


@check50.check(runs)
def six():
    """Does diamonds.c produce a proper 6 tall diamond?"""
    return check(6)


@check50.check(runs)
def seven():
    """Does diamonds.c produce a proper 7 tall diamond?"""
    return check(7)


@check50.check(runs)
def eight():
    """Does diamonds.c produce a proper 8 tall diamond?"""
    return check(8)


@check50.check(runs)
def nine():
    """Does diamonds.c produce a proper 9 tall diamond?"""
    return check(9)


@check50.check(runs)
def ten():
    """Does diamonds.c produce a proper 10 tall diamond?"""
    return check(10)


@check50.check(runs)
def eleven():
    """Does diamonds.c produce a proper 11 tall diamond?"""
    return check(11)


@check50.check(runs)
def twelve():
    """Does diamonds.c produce a proper 12 tall diamond?"""
    return check(12)


@check50.check(runs)
def thirteen():
    """Does diamonds.c produce a proper 13 tall diamond?"""
    return check(13)


@check50.check(runs)
def fourteen():
    """Does diamonds.c produce a proper 14 tall diamond?"""
    return check(14)


@check50.check(runs)
def fifteen():
    """Does diamonds.c produce a proper 15 tall diamond?"""
    return check(15)


@check50.check(runs)
def sixteen():
    """Does diamonds.c produce a proper 16 tall diamond?"""
    return check(16)


@check50.check(runs)
def seventeen():
    """Does diamonds.c produce a proper 17 tall diamond?"""
    return check(17)


@check50.check(runs)
def eighteen():
    """Does diamonds.c produce a proper 18 tall diamond?"""
    return check(18)


@check50.check(runs)
def nineteen():
    """Does diamonds.c produce a proper 19 tall diamond?"""
    return check(19)


@check50.check(runs)
def twenty():
    """Does diamonds.c produce a proper 20 tall diamond?"""
    return check(20)
