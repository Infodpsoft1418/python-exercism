import re


def decode(string):
    return re.sub(r"(\d+)(\D)", lambda m: m.group(2) * int(m.group(1)), string)


def _encode_result(counter, letter):
    if counter > 1:
        return f"{counter}{letter}"
    return letter


def encode(string):
    if len(string) == 0:
        return string
    result = ""
    curr_letter = string[0]
    counter = 0
    for letter in string:
        if letter == curr_letter:
            counter += 1
        else:
            result += _encode_result(counter, curr_letter)
            counter = 1
            curr_letter = letter
    result += _encode_result(counter, curr_letter)
    return result
