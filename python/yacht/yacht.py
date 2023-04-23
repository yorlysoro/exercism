"""
Yacht Dice Game
"""


YACHT = 'YACHT'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 44
LITTLE_STRAIGHT = [1, 2, 3, 4, 5]
BIG_STRAIGHT = [2, 3, 4, 5, 6]
CHOICE = 11


def score(dice, category):
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        counts = dice.count(category)
        return counts * category
    elif category == FOUR_OF_A_KIND:
        repeat_number = [x for x in dice if dice.count(x) >= 4]
        return sum(repeat_number[:4])
    elif category == CHOICE:
        return sum(dice)
    elif category == BIG_STRAIGHT:
        number_2_of_6 = [x for x in dice if x in BIG_STRAIGHT]
        equals = sorted(number_2_of_6) == BIG_STRAIGHT
        return 30 if equals else 0
    elif category == LITTLE_STRAIGHT:
        number_1_of_5 = [x for x in dice if x in LITTLE_STRAIGHT]
        equals = sorted(number_1_of_5) == LITTLE_STRAIGHT
        return 30 if equals else 0
    elif category == FULL_HOUSE:
        numbers = [x for x in dice if dice.count(x) == 2 or dice.count(x) == 3]
        equals = len(numbers) == len(dice)
        return sum(numbers) if equals else 0
    elif category == YACHT:
        numbers = [x for x in dice if dice.count(x) == 5]
        count = len(numbers) == 5
        return 50 if count else 0
