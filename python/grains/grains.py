"""
Number of gains in ches board
"""


def square(n):
    if n < 1 or n > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (n - 1)


def total():
    n = range(0, 64)
    totals = [square(i+1) for i in n]
    return sum(totals)


numbers = [1, 2, 3, 4, 16, 32, 64]

for n in numbers:
    print(square(n), sep=",")
print(total())
