import math
import subprocess
import time
from subprocess import PIPE

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


def print_rowr_with_extra_space(size, spaces):
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
        print_rowr_with_extra_space(current_length, spacing)
        current_length += 1
    if rows % 2 == 1:
        print_rowr_with_extra_space(spacing, spacing)
    while current_length > 1:
        current_length -= 1
        print_rowr_with_extra_space(current_length, spacing)
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
    check50.run("./diamonds").stdin("10").exit()


@check50.check(runs)
def prompts():
    """Does diamonds.c prompt the user properly?"""
    process = subprocess.Popen(["./diamonds"], stdout=subprocess.PIPE, shell=True)
    output = ""
    for line in process.stdout:
        output += line + "\n"
    raise check50.Mismatch(output, output, output)


@check50.check()
def low_value():
    """Does diamonds.c reject a low value?"""
    check50.run("./diamonds").stdin("0").stdout("Size: ")


@check50.check()
def high_value():
    """Does diamonds.c reject a high value?"""
    check50.c.run("./diamonds").stdin("21").stdout("Size: ")


@check50.check()
def one():
    """Does diamonds.c produce a proper 1 tall diamond?"""
    output = check50.run("./diamonds").stdin("1").stdout(timeout=5)
    if get_valid_outputs(1).count(output) != 0:
        pass
    else:
        raise check50.Mismatch(get_valid_outputs(1)[1], output)
