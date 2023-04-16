"""
This module calculate number of steps to get the number one
with the collatz conjecture
"""


def steps(n):
    n = int(n)
    if n < 0:
        raise ValueError("Only positive integers are allowed")
    elif n == 0:
        raise ValueError("Only positive integers are allowed")

    z = n
    steps_count = 0
    while z > 1:
        if z % 2 == 1:
            z = int((3 * z + 1))
        elif z % 2 == 0:
            z = int(z / 2)
        steps_count += 1

    return steps_count


print(steps(12))
