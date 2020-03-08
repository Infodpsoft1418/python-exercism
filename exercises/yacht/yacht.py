from collections import Counter

# Score categories.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def sum_for_ns(dice, n):
    return sum(x for x in dice if x == n)


def full_house(dice):
    counter = Counter(dice)
    return sum(dice) if set(counter.values()) == {3, 2} else 0


def four_of_a_kind(dice):
    counter = Counter(dice)
    number, count = counter.most_common()[0]
    return 4 * number if count >= 4 else 0


def little_straight(dice):
    return 30 if set(dice) == {1, 2, 3, 4, 5} else 0


def big_straight(dice):
    return 30 if set(dice) == {2, 3, 4, 5, 6} else 0


def yacht(dice):
    return 50 if len(set(dice)) == 1 else 0


def score(dice, category):
    if category == YACHT:
        return yacht(dice)
    if category == ONES:
        return sum_for_ns(dice, 1)
    if category == TWOS:
        return sum_for_ns(dice, 2)
    if category == THREES:
        return sum_for_ns(dice, 3)
    if category == FOURS:
        return sum_for_ns(dice, 4)
    if category == FIVES:
        return sum_for_ns(dice, 5)
    if category == SIXES:
        return sum_for_ns(dice, 6)
    if category == FULL_HOUSE:
        return full_house(dice)
    if category == FOUR_OF_A_KIND:
        return four_of_a_kind(dice)
    if category == LITTLE_STRAIGHT:
        return little_straight(dice)
    if category == BIG_STRAIGHT:
        return big_straight(dice)
    if category == CHOICE:
        return sum(dice)
    return 0
