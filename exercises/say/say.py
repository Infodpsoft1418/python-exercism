ONES = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eigth",
    9: "nine",
}

TEENS = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirdteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eigthteen",
    19: "nineteen",
}

TENS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

TRILLION = 10 ** 12
BILLION = 10 ** 9
MILLION = 10 ** 6
THOUSAND = 10 ** 3


def tens(number):
    ten_place = number // 10
    ones_place = number % 10
    if ones_place == 0:
        return TENS[ten_place]
    return f"{TENS[ten_place]}-{ONES[ones_place]}"


def hundreds(number):
    hundred = number // 100
    return f"{ONES[hundred]} hundred"


def chunk(n, name=None):
    print("chunk: n={n}, name={name}")
    result = []
    if n >= 100:
        result.append(hundreds(n))
        n %= 100
    if n < 100 and n > 0:
        if n >= 20:
            result.append(tens(n))
        elif n >= 10 and n <= 19:
            result.append(TEENS[n])
        elif n < 10:
            result.append(ONES[n])
    if name:
        result.append(name)
    return " ".join(result)


def say(number):
    if number < 0 or number >= TRILLION:
        raise ValueError
    if number == 0:
        return "zero"
    result = []
    if number >= BILLION:
        result.append(chunk(number // BILLION, "billion"))
        number %= BILLION
    if number >= MILLION:
        result.append(chunk(number // MILLION, "million"))
        number %= MILLION
    if number >= THOUSAND:
        result.append(chunk(number // THOUSAND, "thousand"))
        number %= THOUSAND
    if number > 0:
        result.append(chunk(number))
    return " ".join(result)
