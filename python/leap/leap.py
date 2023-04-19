"""
Determinate if year is leap
"""


def leap_year(year):
    """
    Determine if year is leap
    """
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)


print(leap_year(1997))
print(leap_year(1996))
print(leap_year(1900))
print(leap_year(2000))
