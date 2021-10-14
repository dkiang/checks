import math

import check50

from check50 import c

simulated_output = ""


def print_row(size, spaces):
    global simulated_output
    spaces = spaces - size
    i = 0
    while i < spaces:
        i += 1
        simulated_output += " "
    printed = 1
    simulated_output += "*"
    while printed < size:
        printed += 1
        simulated_output += " *"
    simulated_output += "\n"


def generate(rows):
    global simulated_output
    simulated_output = ""
    if rows % 2 == 1:
        spacing = math.trunc(rows / 2) + 1
    else:
        spacing = math.trunc(rows / 2)
    length = math.trunc(rows / 2)
    current_length = 1
    while current_length <= length:
        print_row(current_length, spacing)
        current_length += 1
    if rows % 2 == 1:
        print_row(spacing, spacing)
    while current_length > 1:
        current_length -= 1
        print_row(current_length, spacing)
    return simulated_output


def print_row_with_extra_space(size, spaces):
    global simulated_output
    spaces = spaces - size
    i = 0
    while i < spaces:
        i += 1
        simulated_output += " "
    printed = 1
    simulated_output += " *"
    while printed < size:
        printed += 1
        simulated_output += " *"
    simulated_output += "\n"


def generate_with_extra_space(rows):
    global simulated_output
    simulated_output = ""
    if rows % 2 == 1:
        spacing = math.trunc(rows / 2) + 1
    else:
        spacing = math.trunc(rows / 2)
    length = math.trunc(rows / 2)
    current_length = 1
    while current_length <= length:
        print_row_with_extra_space(current_length, spacing)
        current_length += 1
    if rows % 2 == 1:
        print_row_with_extra_space(spacing, spacing)
    while current_length > 1:
        current_length -= 1
        print_row_with_extra_space(current_length, spacing)
    return simulated_output


def get_valid_outputs(rows):
    outputs = [generate(rows), generate_with_extra_space(rows)]
    return outputs


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
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "1").stdout()
    if output in get_valid_outputs(1):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(1)[1], output)

@check50.check(runs)
def two():
    """Does diamonds.c produce a proper 2 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "2").stdout()
    if output in get_valid_outputs(2):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(2)[1], output)

@check50.check(runs)
def three():
    """Does diamonds.c produce a proper 3 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "3").stdout()
    if output in get_valid_outputs(3):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(3)[1], output)

@check50.check(runs)
def four():
    """Does diamonds.c produce a proper 4 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "4").stdout()
    if output in get_valid_outputs(4):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(4)[1], output)

@check50.check(runs)
def five():
    """Does diamonds.c produce a proper 5 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "5").stdout()
    if output in get_valid_outputs(5):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(5)[1], output)

@check50.check(runs)
def six():
    """Does diamonds.c produce a proper 6 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "6").stdout()
    if output in get_valid_outputs(6):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(6)[1], output)

@check50.check(runs)
def seven():
    """Does diamonds.c produce a proper 7 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "7").stdout()
    if output in get_valid_outputs(7):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(7)[1], output)

@check50.check(runs)
def eight():
    """Does diamonds.c produce a proper 8 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "8").stdout()
    if output in get_valid_outputs(8):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(8)[1], output)

@check50.check(runs)
def nine():
    """Does diamonds.c produce a proper 9 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "9").stdout()
    if output in get_valid_outputs(9):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(9)[1], output)

@check50.check(runs)
def ten():
    """Does diamonds.c produce a proper 10 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "10").stdout()
    if output in get_valid_outputs(10):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(10)[1], output)

@check50.check(runs)
def eleven():
    """Does diamonds.c produce a proper 11 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "11").stdout()
    if output in get_valid_outputs(11):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(11)[1], output)

@check50.check(runs)
def twelve():
    """Does diamonds.c produce a proper 12 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "12").stdout()
    if output in get_valid_outputs(12):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(12)[1], output)

@check50.check(runs)
def thirteen():
    """Does diamonds.c produce a proper 13 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "13").stdout()
    if output in get_valid_outputs(13):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(13)[1], output)

@check50.check(runs)
def fourteen():
    """Does diamonds.c produce a proper 14 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "14").stdout()
    if output in get_valid_outputs(14):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(14)[1], output)

@check50.check(runs)
def fifteen():
    """Does diamonds.c produce a proper 15 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "15").stdout()
    if output in get_valid_outputs(15):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(15)[1], output)

@check50.check(runs)
def sixteen():
    """Does diamonds.c produce a proper 16 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "16").stdout()
    if output in get_valid_outputs(16):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(16)[1], output)

@check50.check(runs)
def seventeen():
    """Does diamonds.c produce a proper 17 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "17").stdout()
    if output in get_valid_outputs(17):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(17)[1], output)

@check50.check(runs)
def eighteen():
    """Does diamonds.c produce a proper 18 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "18").stdout()
    if output in get_valid_outputs(18):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(18)[1], output)

@check50.check(runs)
def nineteen():
    """Does diamonds.c produce a proper 19 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "19").stdout()
    if output in get_valid_outputs(19):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(19)[1], output)

@check50.check(runs)
def twenty():
    """Does diamonds.c produce a proper 20 tall diamond?"""
    output = check50.c.run("clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter "
                           "-Wno-unused-variable -Wshadow    diamonds.c  -lcrypt -lcs50 -lm -o diamonds && ./diamonds").stdin(
        "20").stdout()
    if output in get_valid_outputs(20):
        return True
    else:
        raise check50.Mismatch(get_valid_outputs(20)[1], output)

