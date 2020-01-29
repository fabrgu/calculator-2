"""Math functions for calculator."""
from functools import reduce


def add(num1, num2):
    """Return the sum of the two inputs."""

    return num1 + num2


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num1 - num2


def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    return num1 / num2


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2


def add_list(num_list):
    return reduce(add, num_list)


def subtract_list(num_list):
    subtract_counter = num_list[0]
    i = 1
    while i < len(num_list):
        subtract_counter -= num_list[i]
        i += 1
    return subtract_counter


def mult_list(num_list):
    mult_counter = num_list[0]
    i = 1
    while i < len(num_list):
        mult_counter *= num_list[i]
        i += 1
    return mult_counter
