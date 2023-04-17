"""
This module determine if a number is armstrong numbers
"""


def is_armstrong_number(n):
    number_str = str(n)
    number_of_digits = len(number_str)
    result = 0
    for i in range(number_of_digits):
        result += pow(int(number_str[i]), number_of_digits)
    is_armstrong = n == result
    return is_armstrong

def is_armstrong(n):
    number_str = str(n)
    number_of_digits = len(number_str)
    return n == sum([pow(int(number_str[i]), number_of_digits) for i in range(number_of_digits)])

print(is_armstrong_number(100))
