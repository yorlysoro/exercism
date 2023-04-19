"""
Difference of Squares module
"""


def square_of_sum(n):
    """
    Calculate the square of the sum of the first n natural numbers
    """
    return pow(sum(range(1, n+1)), 2)


def sum_of_squares(n):
    return sum([pow(x, 2) for x in range(1, n+1)])


def difference_of_squares(n):
    square_sum = square_of_sum(n)
    sum_square = sum_of_squares(n)
    return square_sum - sum_square


if __name__ == "__main__":
    print(square_of_sum(10))
    print(sum_of_squares(10))
    print(difference_of_squares(10))
