"""
Ghost Gobble Arcade Game Exercism
"""


def eat_ghost(power, ghost):
    return power and ghost


def score(power, dot):
    return power or dot


def lose(power, ghost):
    return not power and ghost


def win(dot, power, ghost):
    loser = lose(power, ghost)
    return (dot and power) or (dot and not loser)


print(eat_ghost(False, True))
print(score(True, True))
print(lose(False, True))
print(win(True, True, True))
