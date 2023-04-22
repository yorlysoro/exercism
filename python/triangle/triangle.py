"""
Module for determine if triangle is scalene, isosceles or equilateral
"""


def scalene(sides):
    if check_inequality(sides):
        if equilateral(sides):
            return False
        elif isosceles(sides):
            return False
        else:
            return True
    else:
        return False


def isosceles(sides):
    if check_inequality(sides):
        if equilateral(sides):
            return True
        else:
            repeat_number = [x for x in sides if sides.count(x) > 1]
            if len(repeat_number) > 0:
                unique_number = [x for x in sides if sides.count(x) == 1]
                result = repeat_number[0] * 2
                return result > unique_number[0]
            else:
                return False
    else:
        return False


def equilateral(sides):
    if check_inequality(sides):
        return (3 * max(sides)) == sum(sides)
    else:
        return False


def check_inequality(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return (a + b - c) * (a + c - b) * (b + c - a) > 0


print(equilateral([1, 1, 1]))
print(isosceles([1, 3, 3]))
print(scalene([5, 4, 6]))
