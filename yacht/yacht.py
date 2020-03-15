# Score categories.
# Change the values as you see fit.
YACHT = lambda x: 50 if len(x) == 1 else 0
ONES = lambda x: x[1]
TWOS = lambda x: x[2] * 2
THREES = lambda x: x[3] * 3
FOURS = lambda x: x[4] * 4
FIVES = lambda x: x[5] * 5
SIXES = lambda x: x[6] * 6
FULL_HOUSE = lambda x: sum(x.elements()) if len(x) == 2 and x.most_common()[0][1] == 3 else 0
FOUR_OF_A_KIND = lambda x: 4 * x.most_common()[0][0] if x.most_common()[0][1] >= 4 else 0
LITTLE_STRAIGHT = lambda x: 30 if len(x) == 5 and sum(x.elements()) == 15 else 0
BIG_STRAIGHT = lambda x: 30 if len(x) == 5 and sum(x.elements()) == 20 else 0
CHOICE = lambda x: sum(x.elements())

from collections import Counter

def score(dice, category):
    return category(Counter(dice))
